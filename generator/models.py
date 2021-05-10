from django.db import models
from accounts.models import *

class problem(models.Model):
    problem_id = models.BigAutoField(primary_key=True)
    ID = models.ForeignKey(monitor, on_delete=models.CASCADE)
    answer = models.IntegerField()
    type = models.CharField(max_length=20)
    blank_num = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    blank_text = models.TextField(blank=True, null=True)


