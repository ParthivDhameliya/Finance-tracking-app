from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from creditManagement.api.serializers import CreditCardAccountSerializer, LoanAccountSerializer, LenderSerializer, LendersListSerializer
from rest_framework.permissions import AllowAny
from creditManagement.models import LoanAccount, CreditCardAccount, Lender
from authentication.models import UserAccount

# Credit card views 
class CreditAccountsView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = CreditCardAccount.objects.all()
    serializer_class = CreditCardAccountSerializer


class CreditAccountsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreditCardAccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return CreditCardAccount.objects.filter(owner=owner)

class CreditAccountCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreditCardAccountSerializer

    def perform_create(self, serializer):
        owner = self.kwargs.get('owner')
        owner_useraccount = UserAccount.objects.get(id=owner)

        serializer.save(owner=owner_useraccount)


class CreditAccountView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CreditCardAccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        owner_useraccount = UserAccount.objects.get(id=owner)        
        creditCardID = self.kwargs['creditCardID']
        return CreditCardAccount.objects.filter(owner=owner_useraccount).filter(creditCardID=creditCardID)       


# Loan account views
class LoanAccountsView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = LoanAccount.objects.all()
    serializer_class = LoanAccountSerializer


class LoanAccountCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoanAccountSerializer

    def perform_create(self, serializer):
        owner = self.kwargs.get('owner')
        owner_useraccount = UserAccount.objects.get(id=owner)

        serializer.save(owner=owner_useraccount)


class LoanAccountsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoanAccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return LoanAccount.objects.filter(owner=owner)
    

class LoanAccountView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoanAccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        owner_useraccount = UserAccount.objects.get(id=owner)        
        loanID = self.kwargs['loanID']
        return LoanAccount.objects.filter(owner=owner_useraccount).filter(loanID=loanID) 

# Lender views
class LendersView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer


class LendersListView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Lender.objects.all()
    serializer_class = LendersListSerializer