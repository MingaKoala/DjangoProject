from django.contrib import admin

#from mysite.polls.models import Choice, Poll /// dont run

from .models import Choice, Poll



admin.site.register(Poll)
admin.site.register(Choice)