from django.db import models
from accounts.models import Account
from creditManagement.models import CreditCardAccount

# Create your models here.

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        WITHDRAW = 'Withdraw'
        DEPOSIT = 'Deposit'

    transID = models.AutoField(primary_key=True)
    transDate = models.DateField(max_length= 50, blank=False)
    transAmount = models.DecimalField(max_digits=10, blank=False, decimal_places=2)
    transDescription = models.CharField(max_length=50)
    transType = models.CharField(max_length=10, choices=TransactionType.choices, default=TransactionType.WITHDRAW)
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_transactions")

    def __str__(self):
        return self.transID


class CreditCardTransaction(models.Model):
    creditTransID = models.AutoField(primary_key=True)
    transDate = models.DateField(max_length=50, blank=False)
    transAmount = models.DecimalField(max_digits=10, decimal_places=2)
    transDescription = models.TextField(max_length=50)
    category = models.CharField(max_length=255, blank=True, null=True)
    is_expense = models.BooleanField(default=True)
    creditCard = models.ForeignKey(CreditCardAccount, on_delete=models.CASCADE, related_name="credit_card_transactions")

    def __str__(self):  
        return self.creditTransID
