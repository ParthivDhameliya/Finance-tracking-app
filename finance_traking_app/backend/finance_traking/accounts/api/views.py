from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.api.serializers import AccountSerializer
from rest_framework.permissions import AllowAny
from accounts.models import Account
from authentication.models import UserAccount

class AccountsView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountsListingView(ListAPIView):
    # queryset = Account.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = AccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Account.objects.filter(owner=owner)
    
    
class AccountCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        owner = self.kwargs.get('owner')
        owner_useraccount = UserAccount.objects.get(id=owner)

        serializer.save(owner=owner_useraccount)


class AccountDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AccountSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        owner = self.kwargs['owner']
        owner_useraccount = UserAccount.objects.get(id=owner)        
        accID = self.kwargs['accID']
        return Account.objects.filter(owner=owner_useraccount).filter(accountID=accID)    