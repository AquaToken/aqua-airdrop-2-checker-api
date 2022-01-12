from django.urls import path

from aqua_airdrop2_checker.airdrop2.views import SnapshotAccountAPI


urlpatterns = [
    path('snapshot/<slug:account_id>/', SnapshotAccountAPI.as_view()),
]
