# Generated by Django 4.0.1 on 2022-01-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirdropAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(db_index=True, max_length=56, unique=True)),
                ('native_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('yxlm_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('aqua_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('native_pool_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('yxlm_pool_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('aqua_pool_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('aqua_lock_balance', models.DecimalField(decimal_places=7, max_digits=20)),
                ('aqua_lock_term', models.PositiveIntegerField()),
                ('airdrop_shares', models.DecimalField(decimal_places=7, max_digits=20)),
                ('airdrop_reward', models.DecimalField(decimal_places=7, max_digits=20)),
            ],
        ),
    ]
