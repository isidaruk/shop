from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    # "slug" field value is automatically set using the value of "name" field.
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'stock', 'avaliable', 'created', 'updated']
    list_filter = ['avaliable', 'created', 'updated']
    list_editable = ['price', 'stock', 'avaliable']
    prepopulated_fields = {'slug': ('name',)}
