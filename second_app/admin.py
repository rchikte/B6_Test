from django.contrib import admin
from .models import Department, Student,College,Principal, Subject

admin.site.register([Student,College,Principal,Department,Subject])

# Register your models here.
