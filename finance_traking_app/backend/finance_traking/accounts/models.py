from django.db import models
from authentication.models import UserAccount

# Create your models here.

class Account(models.Model):
    class AccountType(models.TextChoices):
        CHEQUING = 'Chequing'
        SAVING = 'Saving'

    accountID = models.AutoField(primary_key=True)
    accountNumber = models.IntegerField()
    accountType = models.CharField(max_length=50, choices=AccountType.choices, default=AccountType.CHEQUING)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='accounts')   

    def __str__(self):
        return (str)(self.accountID)

    