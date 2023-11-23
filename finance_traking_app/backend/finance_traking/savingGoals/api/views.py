from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from savingGoals.api.serializers import SavingGoalsSerializer
from rest_framework.permissions import AllowAny
from savingGoals.models import SavingsGoal
from accounts.models import Account

# Credit card views 
class SavingGoalsView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingGoalsSerializer


class SavingGoalsListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SavingGoalsSerializer
    lookup_field = 'account'

    def get_queryset(self):
        account = self.kwargs['accID']
        return SavingsGoal.objects.filter(account=account)

class SavingGoalsCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SavingGoalsSerializer

    def perform_create(self, serializer):
        account = self.kwargs.get('accID')
        accountID = Account.objects.get(accountID=account)

        serializer.save(account=accountID)

class SavingGoalDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SavingGoalsSerializer
    lookup_field = 'goalID'

    def get_queryset(self):
        account = self.kwargs['accID']     
        goalID = self.kwargs['goalID']
        return SavingsGoal.objects.filter(account=account).filter(goalID=goalID)  