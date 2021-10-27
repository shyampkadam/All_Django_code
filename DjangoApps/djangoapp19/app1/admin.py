from django.contrib import admin

from app1.models import Employee,RegularEmployee,ContractEmployee

admin.site.register(Employee)
admin.site.register(RegularEmployee)
admin.site.register(ContractEmployee)