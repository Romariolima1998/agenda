from django.contrib import admin

from contact.models import Contact
from contact.models import Category
# Register your models here.


@admin.register(Contact)
class ContactAdimin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    ordering = ('-id',)
    list_filter = ('created_date',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = 10
    list_max_show_all = 100
    # list_editable = 'first_name', 'last_name',
    list_display_links = ('first_name', 'id')


@admin.register(Category)
class CategoryAdimin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)
