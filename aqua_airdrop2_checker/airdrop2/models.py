from django.db import models


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

    def __str__(self):
        return self.account_id
