from rest_framework import serializers

from aqua_airdrop2_checker.airdrop2.models import AirdropAccount


class AirdropAccountSerializer(serializers.ModelSerializer):
    raw_airdrop_shares = serializers.DecimalField(max_digits=20, decimal_places=7)
    raw_airdrop_reward = serializers.DecimalField(max_digits=20, decimal_places=7)
    airdrop_boost = serializers.DecimalField(max_digits=20, decimal_places=7)

    class Meta:
        model = AirdropAccount
        fields = ['account_id', 'native_balance', 'yxlm_balance', 'aqua_balance',
                  'native_pool_balance', 'yxlm_pool_balance', 'aqua_pool_balance',
                  'aqua_lock_balance', 'aqua_lock_term', 'airdrop_shares', 'airdrop_reward',
                  'raw_airdrop_shares', 'raw_airdrop_reward', 'airdrop_boost']
