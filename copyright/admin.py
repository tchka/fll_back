from django.contrib import admin

from .models import Category, CopyrighterLevel, JobStatus, Job

admin.site.register(Category)
admin.site.register(CopyrighterLevel)
admin.site.register(JobStatus)
admin.site.register(Job)
