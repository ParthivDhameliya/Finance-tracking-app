from django.urls import path
from accounts.api.views import AccountDetailsView, AccountsView, AccountCreateView, AccountsListingView

urlpatterns = [
    path('', AccountsView.as_view(), name="accounts"),
    path('<int:owner>/', AccountsListingView.as_view(), name="account"),
    path('<int:owner>/<int:accID>/', AccountDetailsView.as_view(), name="account"),
    path('<int:owner>/create-account/', AccountCreateView.as_view(), name="account_create"),
]
