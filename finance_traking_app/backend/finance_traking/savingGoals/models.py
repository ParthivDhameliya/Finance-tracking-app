from django.db import models
from accounts.models import Account

# Create your models here.
class SavingsGoal(models.Model):
    goalID = models.AutoField(primary_key=True)
    goalName = models.CharField(blank=False, max_length=30)
    goalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='savingGoals')

    def __str__(self):
        return self.goalName
