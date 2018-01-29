from django.contrib import admin
from rango.models import Page, Category

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)