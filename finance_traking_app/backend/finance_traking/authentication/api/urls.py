from django.urls import path
from authentication.api.views import SignupView, Accounts, AccountDetails

urlpatterns = [
    path('', Accounts.as_view(), name='user_accounts'),
    path('<int:pk>/', AccountDetails.as_view(), name='user_account'),
    path('signup/', SignupView.as_view(), name="signup"),
]
