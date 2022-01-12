from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin

from aqua_airdrop2_checker.airdrop2.models import AirdropAccount
from aqua_airdrop2_checker.airdrop2.serializers import AirdropAccountSerializer


class SnapshotAccountAPI(RetrieveModelMixin, GenericAPIView):
    queryset = AirdropAccount.objects.all()
    serializer_class = AirdropAccountSerializer
    lookup_field = 'account_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
