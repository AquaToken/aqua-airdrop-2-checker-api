from decimal import Decimal

from constance import config
from django.conf import settings
from django.db import models


class AirdropAccountQuerySet(models.QuerySet):
    def stats(self):
        return self.aggregate(
            accounts=models.Count('account_id'),
            total_xlm=models.Sum(models.F('native_balance') + models.F('yxlm_balance')
                                 + models.F('native_pool_balance') + models.F('yxlm_pool_balance')),
            total_aqua=models.Sum(models.F('aqua_balance') + models.F('aqua_pool_balance')
                                  + models.F('aqua_lock_balance')),
            total_shares=models.Sum('airdrop_shares'),
            locked_aqua=models.Sum('aqua_lock_balance'),
            accounts_with_lock=models.Count(models.Case(
                models.When(aqua_lock_balance__gt=0, then=1),
                default=None,
            )),
        )


class AirdropAccount(models.Model):
    account_id = models.CharField(max_length=56, unique=True, db_index=True)

    native_balance = models.DecimalField(max_digits=20, decimal_places=7)
    yxlm_balance = models.DecimalField(max_digits=20, decimal_places=7)
    aqua_balance = models.DecimalField(max_digits=20, decimal_places=7)

    native_pool_balance = models.DecimalField(max_digits=20, decimal_places=7)
    yxlm_pool_balance = models.DecimalField(max_digits=20, decimal_places=7)
    aqua_pool_balance = models.DecimalField(max_digits=20, decimal_places=7)

    aqua_lock_balance = models.DecimalField(max_digits=20, decimal_places=7)
    aqua_lock_term = models.PositiveIntegerField()

    airdrop_shares = models.DecimalField(max_digits=20, decimal_places=7)
    airdrop_reward = models.DecimalField(max_digits=20, decimal_places=7)

    objects = AirdropAccountQuerySet.as_manager()

    def __str__(self):
        return self.account_id

    @property
    def locked_share(self):
        return self.aqua_lock_balance * config.AQUA_PRICE

    @property
    def unlocked_share(self):
        xlm_balance = self.native_balance + self.yxlm_balance + self.native_pool_balance + self.yxlm_pool_balance
        aqua_balance = self.aqua_balance + self.aqua_pool_balance
        return xlm_balance + aqua_balance * config.AQUA_PRICE

    @property
    def raw_airdrop_shares(self):
        return self.locked_share + self.unlocked_share

    @property
    def raw_airdrop_reward(self):
        reward = self.raw_airdrop_shares * config.SHARE_PRICE

        if reward > config.REWARD_CAP and self.account_id not in settings.REWARD_CAP_EXCEPTIONS:
            reward = config.REWARD_CAP

        return reward

    @property
    def airdrop_boost(self):
        locked_share = self.locked_share
        unlocked_share = self.unlocked_share

        time_lock_multiplier = Decimal(min(self.aqua_lock_term, config.MAX_LOCK_TERM) / config.MAX_LOCK_TERM)
        value_lock_multiplier = min(locked_share, unlocked_share) / unlocked_share
        total_lock_multiplier = time_lock_multiplier * value_lock_multiplier

        return Decimal(total_lock_multiplier * config.MAX_LOCK_BOOST)
