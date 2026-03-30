from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(recipe)

admin.site.register(Department)
admin.site.register(studentID)
admin.site.register(Student)