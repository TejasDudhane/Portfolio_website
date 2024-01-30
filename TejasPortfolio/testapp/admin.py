from django.contrib import admin
from testapp.models import ContactDb
class ContactDbAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']
admin.site.register(ContactDb,ContactDbAdmin)