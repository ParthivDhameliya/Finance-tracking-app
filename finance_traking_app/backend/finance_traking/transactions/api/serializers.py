from rest_framework import serializers
from transactions.models import Transaction, CreditCardTransaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transDate', 'transAmount', 'transDescription', 'transType']


class CreditCardTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCardTransaction
        fields = ['transDate', 'transAmount', 'transDescription', 'category', 'is_expense']
        