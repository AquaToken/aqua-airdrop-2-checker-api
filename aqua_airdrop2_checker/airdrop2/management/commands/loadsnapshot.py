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
        fields = ['account_id', 'native_balance', 'yxlm_balance', 'aqua_balance',
                  'native_pool_balance', 'yxlm_pool_balance', 'aqua_pool_balance',
                  'aqua_lock_balance', 'aqua_lock_term', 'airdrop_shares', 'airdrop_reward']

        return AirdropAccount(**dict(
            zip(fields, raw_account),
        ))

    def save_snapshot_to_db(self, snapshot: Iterable[AirdropAccount]):
        batch = []
        for account in snapshot:
            batch.append(account)

            if len(batch) >= self.BATCH_SIZE:
                AirdropAccount.objects.bulk_create(batch)
                batch = []

        if len(batch) > 0:
            AirdropAccount.objects.bulk_create(batch)
