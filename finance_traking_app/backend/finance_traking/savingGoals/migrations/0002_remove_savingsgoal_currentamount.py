# Generated by Django 4.2.7 on 2023-11-23 04:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("savingGoals", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="savingsgoal",
            name="currentAmount",
        ),
    ]