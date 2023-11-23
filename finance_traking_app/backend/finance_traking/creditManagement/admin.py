from django.contrib import admin
from creditManagement.models import CreditCardAccount, Lender, LoanAccount
# Register your models here.

class CreditCardAccountAdmin(admin.ModelAdmin):
    list_display = ['creditCardID', 'cardNumber', 'cardHolderName', 'cardType', 'creditLimit', 'availableCredit', 'paymentDueDate', 'billing_cycle_start', 'billing_cycle_end', 'owner']
    list_filter = ('owner', )

class LenderAdmin(admin.ModelAdmin):
    list_display = ['lenderID', 'lenderName', 'contactEmail', 'contactPhone', 'address']
    list_filter = ('lenderName', )

class LoanAccountAdmin(admin.ModelAdmin):
    list_display = ['loanID', 'loanAmount', 'interestRate', 'loanTerm', 'paymentFrequency', 'paymentStartDate', 'owner', 'lender']
    list_filter = ('owner', 'lender', )

admin.site.register(CreditCardAccount, CreditCardAccountAdmin)
admin.site.register(Lender, LenderAdmin)
admin.site.register(LoanAccount, LoanAccountAdmin)