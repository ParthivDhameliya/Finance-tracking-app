from django.contrib import admin
from transactions.models import Transaction, CreditCardTransaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transID', 'transDate', 'transAmount', 'transDescription', 'transType', 'accountID']

class CreditCardTransactionAdmin(admin.ModelAdmin):
    list_display = ['creditTransID', 'transDate', 'transAmount', 'transDescription', 'category', 'is_expense', 'creditCard']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCardTransaction, CreditCardTransactionAdmin)