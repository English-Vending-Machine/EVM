from django.db import models

class user(models.Model):
    ID = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)

class problem_type(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

class problem(models.Model):
    problem_id = models.BigAutoField(primary_key=True)
    ID = models.ForeignKey(user, on_delete=models.CASCADE)
    answer = models.IntegerField()
    type = models.ForeignKey(problem_type, on_delete=models.CASCADE)
    blank_num = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    blank_text = models.TextField(blank=True, null=True)


