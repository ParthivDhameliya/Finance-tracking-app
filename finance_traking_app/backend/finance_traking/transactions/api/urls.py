from django.urls import path
from transactions.api.views import TransactionCreateView, TransactionView, CreditTransactionView, CreditTransactionCreateView

urlpatterns = [
    path('<int:accID>/', TransactionView.as_view(), name="account_transactions_list"),
    path('<int:accID>/create-transaction/', TransactionCreateView.as_view(), name="transactions_create"),
    path('<int:accID>/credit', CreditTransactionView.as_view(), name="credit_transactions_list"),
    path('<int:accID>/create-credit-transaction/', CreditTransactionCreateView.as_view(), name="credit_transactions_create"),
]
