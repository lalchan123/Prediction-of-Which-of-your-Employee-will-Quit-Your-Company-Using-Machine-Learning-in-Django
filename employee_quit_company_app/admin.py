from django.contrib import admin
from .models import EmployeeQuit
# Register your models here.
class EmployeeQuitAdmin(admin.ModelAdmin):
    list_display = ('number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','department','salary','satisfaction_level','last_evaluation','left')
    list_filter = ('left',)

admin.site.register(EmployeeQuit,EmployeeQuitAdmin)