from django.contrib import admin

# Register your models here.
from .models import course,student,grade

admin.site.register(course)
admin.site.register(student)
admin.site.register(grade)