from django.urls import path
from creditManagement.api.views import CreditAccountsView, CreditAccountCreateView, CreditAccountsListView, CreditAccountView, LoanAccountsView, LoanAccountCreateView, LoanAccountsListView, LoanAccountView, LendersView, LendersListView

urlpatterns = [
    # Credit card urls
    path('creditAccounts/', CreditAccountsView.as_view(), name='credit_accounts'),
    path('<int:owner>/creditAccounts/', CreditAccountsListView.as_view(), name="user_personal_accounts"),
    path('<int:owner>/<int:creditCardID>/creditAccounts/', CreditAccountView.as_view(), name="user_single_account"),
    path('<int:owner>/creditCreateAccount/', CreditAccountCreateView.as_view(), name="credit_account_create"),
    # Loan account urls
    path('loanAccounts/', LoanAccountsView.as_view(), name='loan_accounts'),
    path('<int:owner>/loanCreateAccount/', LoanAccountCreateView.as_view(), name="loan_account_create"),
    path('<int:owner>/loanAccounts/', LoanAccountsListView.as_view(), name="user_personal_loan_accounts"),
    path('<int:owner>/<int:loanID>/loanAccounts/', LoanAccountView.as_view(), name="user_single_loan_account"),
    # Lender urls
    path('lenders/', LendersView.as_view(), name='lenders_list'),
    path('lendersList/', LendersListView.as_view(), name='users_lenders_list'),
]
