from rest_framework import serializers
from authentication.models import UserAccount
from accounts.api.serializers import AccountSerializer
from creditManagement.api.serializers import CreditCardAccountSerializer, LoanAccountSerializer
from savingGoals.api.serializers import SavingGoalsSerializer

class UserAccountSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)
    creditCardAccounts = CreditCardAccountSerializer(many=True, read_only=True) 
    loanAccounts = LoanAccountSerializer(many=True, read_only=True)
    savingGoals = SavingGoalsSerializer(many=True, read_only=True)

    class Meta:
        model = UserAccount
        fields = ['name', 'email', 'accounts', 'creditCardAccounts', 'loanAccounts', 'savingGoals']
