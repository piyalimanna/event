from django.contrib import admin

# Register your models here.

from .models import UserProfile, Question

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Question)
