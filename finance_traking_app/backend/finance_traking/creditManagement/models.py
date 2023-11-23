from django.db import models
from authentication.models import UserAccount

# Create your models here.

class CreditCardAccount(models.Model):
    class CardType(models.TextChoices):
        VISA = 'Visa'
        MC = 'MasterCard'
        AMEX = 'American express'
        OTHER = 'Other'

    creditCardID = models.AutoField(primary_key=True)
    cardNumber = models.CharField(max_length=16)  # Last 4 digits may be sufficient for display
    cardHolderName = models.CharField(max_length=255)
    cardType = models.CharField(choices=CardType.choices, max_length=20, default=CardType.VISA)  # Visa, MasterCard, etc.
    creditLimit = models.DecimalField(max_digits=10, decimal_places=2)
    availableCredit = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDueDate = models.DateField()
    billing_cycle_start = models.DateField()
    billing_cycle_end = models.DateField()
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="creditCardAccounts")

    def __str__(self):
        return self.cardNumber
    

class Lender(models.Model):
    lenderID = models.AutoField(primary_key=True)
    lenderName = models.CharField(max_length=255)
    contactEmail = models.EmailField()
    contactPhone = models.CharField(max_length=20)
    address = models.TextField(max_length=100)

    def __str__(self):
        return self.lenderName


class LoanAccount(models.Model):
    class PaymentFrequency(models.TextChoices):
        WEEKLY = 'Weekly'
        BYWEEKLY = 'By-weekly'
        MONTHLY = 'Monthly'
        QUARTERLY = 'Quartrly'

    loanID = models.AutoField(primary_key=True)
    loanAmount = models.DecimalField(max_digits=10, decimal_places=2)
    interestRate = models.DecimalField(max_digits=5, decimal_places=2)
    loanTerm = models.PositiveIntegerField()  # Loan term in months
    paymentFrequency = models.CharField(choices=PaymentFrequency.choices, max_length=20, default=PaymentFrequency.MONTHLY)
    paymentStartDate = models.DateField()
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='loanAccounts')
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, related_name='lenders_accounts')

    def __str__(self):
        return self.loanID
    
