from django.contrib import admin

class AccountsAdmin(admin.ModelAdmin):
    fields = ('email', 'name', 'date_joined')