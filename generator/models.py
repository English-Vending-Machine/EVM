from django.db import models
from accounts.models import *

class problem(models.Model):
    problem_id = models.CharField(primary_key=True, max_length=13)
    ID = models.ForeignKey(monitor, on_delete=models.CASCADE)
    answer = models.IntegerField()
    type = models.CharField(max_length=20)
    blank_num = models.IntegerField()
    image = models.ImageField(upload_to='problems/',null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    blank_text = models.TextField(blank=True, null=True)

class class_cnt(models.Model):
    class_cnt_id = models.IntegerField(primary_key=True, default=1)
    problem_cnt = models.BigIntegerField(default=1)


