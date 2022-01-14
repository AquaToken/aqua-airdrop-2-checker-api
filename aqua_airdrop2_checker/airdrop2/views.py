from decimal import Decimal

from constance import config
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from aqua_airdrop2_checker.airdrop2.models import AirdropAccount
from aqua_airdrop2_checker.airdrop2.serializers import AirdropAccountSerializer


class SnapshotAccountAPI(RetrieveModelMixin, GenericAPIView):
    queryset = AirdropAccount.objects.all()
    serializer_class = AirdropAccountSerializer
    lookup_field = 'account_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SnapshotStatsAPI(APIView):
    def get(self, request, *args, **kwargs):
        stats = AirdropAccount.objects.all().stats()
        data = stats | {
            'aqua_price': config.AQUA_PRICE,
            'share_price': config.SHARE_PRICE,
            'timestamp': config.SNAPSHOT_TIME,
        }

        data = {
            key: str(value) if isinstance(value, Decimal) else value
            for key, value in data.items()
        }

        return Response(data)
