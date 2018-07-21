from django.contrib import admin
from .models import Employer, Job, EmailSubscriber

admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(EmailSubscriber)
