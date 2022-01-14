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
