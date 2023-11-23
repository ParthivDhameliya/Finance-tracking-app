from django.urls import path
from savingGoals.api.views import SavingGoalsView, SavingGoalsListView, SavingGoalsCreateView, SavingGoalDetailsView

urlpatterns = [
    # Credit card urls
    path('savingGoals/', SavingGoalsView.as_view(), name='saving_goals'),
    path('<int:accID>/savingGoals/', SavingGoalsListView.as_view(), name="user_personal_goals"),
    path('<int:accID>/<int:goalID>/savingGoal', SavingGoalDetailsView.as_view(), name="user_single_goal"),
    path('<int:accID>/createSavingGoals/', SavingGoalsCreateView.as_view(), name="create_saving_goal")
]
