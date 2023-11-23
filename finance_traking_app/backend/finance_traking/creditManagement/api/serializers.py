from rest_framework import serializers
from creditManagement.models import CreditCardAccount, LoanAccount, Lender
from transactions.api.serializers import CreditCardTransactionSerializer

class CreditCardAccountSerializer(serializers.ModelSerializer):
    credit_card_transactions = CreditCardTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = CreditCardAccount
        fields = ['cardNumber', 'cardHolderName', 'cardType', 'creditLimit', 'availableCredit', 'paymentDueDate', 
                  'billing_cycle_start', 'billing_cycle_end', 'credit_card_transactions']

class LoanAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAccount
        fields = ['loanID', 'loanAmount', 'interestRate', 'loanTerm', 'paymentFrequency', 'paymentStartDate', 'lender']

class LenderSerializer(serializers.ModelSerializer):
    lenders_accounts = LoanAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Lender
        fields = ['lenderName', 'contactEmail', 'contactPhone', 'lenders_accounts']

class LendersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ['lenderName', 'contactEmail', 'contactPhone', 'address']