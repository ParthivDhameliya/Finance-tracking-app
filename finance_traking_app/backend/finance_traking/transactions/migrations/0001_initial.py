# Generated by Django 4.2.7 on 2023-11-22 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("creditManagement", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("transID", models.AutoField(primary_key=True, serialize=False)),
                ("transDate", models.DateField(max_length=50)),
                ("transAmount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("transDescription", models.CharField(max_length=50)),
                (
                    "transType",
                    models.CharField(
                        choices=[("Withdraw", "Withdraw"), ("Deposit", "Deposit")],
                        default="Withdraw",
                        max_length=10,
                    ),
                ),
                (
                    "accountID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_transactions",
                        to="accounts.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CreditCardTransaction",
            fields=[
                ("creditTransID", models.AutoField(primary_key=True, serialize=False)),
                ("transDate", models.DateField(max_length=50)),
                ("transAmount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("transDescription", models.TextField(max_length=50)),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                ("is_expense", models.BooleanField(default=True)),
                (
                    "creditCard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credit_card_transactions",
                        to="creditManagement.creditcardaccount",
                    ),
                ),
            ],
        ),
    ]
