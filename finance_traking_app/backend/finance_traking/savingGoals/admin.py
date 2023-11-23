from django.contrib import admin
from savingGoals.models import SavingsGoal

# Register your models here.

class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ['goalID', 'goalName', 'goalAmount', 'description', 'account']
    list_filter = ('goalName', 'account', )

admin.site.register(SavingsGoal, SavingsGoalAdmin)
