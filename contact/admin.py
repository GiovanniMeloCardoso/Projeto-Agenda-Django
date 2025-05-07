from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'phone', 'email', 'created_date', 'description')
    ordering = ('id',)
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'description')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('first_name','last_name')