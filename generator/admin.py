from django.contrib import admin
from .models import *

admin.site.register(user)
admin.site.register(problem)
admin.site.register(problem_type)