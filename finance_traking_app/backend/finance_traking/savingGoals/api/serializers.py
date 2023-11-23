from rest_framework import serializers
from savingGoals.models import SavingsGoal

class SavingGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = ['goalName', 'goalAmount', 'description']
