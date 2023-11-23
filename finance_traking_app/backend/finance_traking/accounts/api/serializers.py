from accounts.models import Account
from rest_framework import serializers
from transactions.api.serializers import TransactionSerializer

class AccountSerializer(serializers.ModelSerializer):
    account_transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['accountID', 'accountNumber', 'accountType', 'account_transactions']
        