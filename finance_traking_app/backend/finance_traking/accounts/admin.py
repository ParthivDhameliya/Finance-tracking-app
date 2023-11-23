from django.contrib import admin
from accounts.models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['accountID', 'accountNumber', 'accountType', 'owner']
    list_filter = ('owner', )

admin.site.register(Account, AccountAdmin)
