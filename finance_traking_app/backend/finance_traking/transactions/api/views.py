from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from transactions.api.serializers import TransactionSerializer, CreditCardTransactionSerializer
from transactions.models import Transaction, CreditCardTransaction
from accounts.models import Account
from creditManagement.models import CreditCardAccount

class TransactionView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = TransactionSerializer
    lookup_field = 'accountID'

    def get_queryset(self):
        accID = self.kwargs['accID']
        return Transaction.objects.filter(accountID=accID)
    

class CreditTransactionView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreditCardTransactionSerializer
    lookup_field = 'creditCard'

    def get_queryset(self):
        accID = self.kwargs['accID']
        return CreditCardTransaction.objects.filter(creditCard=accID)
    

class TransactionCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = TransactionSerializer
    lookup_field = 'accountID'

    def perform_create(self, serializer):
        accID = self.kwargs.get('accID')
        account = Account.objects.get(accountID=accID)
        serializer.save(accountID=account)


class CreditTransactionCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreditCardTransactionSerializer
    lookup_field = 'creditCard'

    def perform_create(self, serializer):
        accID = self.kwargs.get('accID')
        account = CreditCardAccount.objects.get(creditCardID=accID)
        serializer.save(creditCard=account)