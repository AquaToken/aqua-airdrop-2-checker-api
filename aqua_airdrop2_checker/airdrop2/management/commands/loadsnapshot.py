from argparse import ArgumentParser
from typing import Iterable

from django.core.management import BaseCommand

from aqua_airdrop2_checker.airdrop2.models import AirdropAccount


class Command(BaseCommand):
    BATCH_SIZE = 1000

    def add_arguments(self, parser: ArgumentParser):
        super(Command, self).add_arguments(parser)

        parser.add_argument('snapshot')

    def handle(self, *args, **options):
        self.save_snapshot_to_db(
            map(
                self.parse_raw_account,
                self.load_snapshot_from_file(options['snapshot']),
            ),
        )

    def load_snapshot_from_file(self, snapshot_file: str) -> Iterable[tuple[str]]:
        with open(snapshot_file, 'r') as f:
            for line in f.readlines():
                if not line.strip().startswith('G'):
                    # Skip headers
                    continue

                yield [cell.strip() for cell in line.strip().split(',')]

    def parse_raw_account(self, raw_account: tuple[str]) -> AirdropAccount:
        return AirdropAccount(
            account_id=raw_account[0],

            native_balance=raw_account[1],
            yxlm_balance=raw_account[2],
            aqua_balance=raw_account[3],

            native_pool_balance=raw_account[4],
            yxlm_pool_balance=raw_account[5],
            aqua_pool_balance=raw_account[6],

            aqua_lock_balance=raw_account[7],
            aqua_lock_term=raw_account[8],

            airdrop_shares=raw_account[9],
            airdrop_reward=raw_account[10],
        )

    def save_snapshot_to_db(self, snapshot: Iterable[AirdropAccount]):
        batch = []
        for account in snapshot:
            batch.append(account)

            if len(batch) >= self.BATCH_SIZE:
                AirdropAccount.objects.bulk_create(batch)
                batch = []

        if len(batch) > 0:
            AirdropAccount.objects.bulk_create(batch)
