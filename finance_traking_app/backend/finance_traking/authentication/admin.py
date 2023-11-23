from django.contrib import admin
from authentication.models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

admin.site.register(UserAccount, UserAccountAdmin)