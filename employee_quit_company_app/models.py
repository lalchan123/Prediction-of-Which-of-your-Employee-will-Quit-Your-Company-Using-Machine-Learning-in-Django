from django.db import models

# Create your models here.
class EmployeeQuit(models.Model):
    number_project = models.FloatField()
    average_montly_hours = models.FloatField()
    time_spend_company = models.FloatField()
    Work_accident = models.FloatField()
    promotion_last_5years = models.FloatField()
    department = models.FloatField()
    salary = models.FloatField()
    satisfaction_level = models.FloatField()
    last_evaluation = models.FloatField()
    left = models.CharField(max_length=50)