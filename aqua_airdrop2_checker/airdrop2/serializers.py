from rest_framework import serializers

from aqua_airdrop2_checker.airdrop2.models import AirdropAccount


class AirdropAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirdropAccount
        fields = ['account_id', 'native_balance', 'yxlm_balance', 'aqua_balance',
                  'native_pool_balance', 'yxlm_pool_balance', 'aqua_pool_balance',
                  'aqua_lock_balance', 'aqua_lock_term', 'airdrop_shares', 'airdrop_reward']
