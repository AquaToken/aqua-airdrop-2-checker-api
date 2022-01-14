from django.urls import path

from aqua_airdrop2_checker.airdrop2.views import SnapshotAccountAPI, SnapshotStatsAPI


urlpatterns = [
    path('snapshot/stats/', SnapshotStatsAPI.as_view()),
    path('snapshot/<slug:account_id>/', SnapshotAccountAPI.as_view()),
]
