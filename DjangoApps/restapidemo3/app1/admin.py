from django.contrib import admin
from app1.models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','fullName','city','salary']