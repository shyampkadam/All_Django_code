from django.contrib import admin

# Register your models here.
from app1.models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'pub_date', 'author','isbn','storename']