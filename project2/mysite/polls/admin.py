from django.contrib import admin

from project2.mysite.tt1.models import Place
from .models import Question

admin.site.register(Question)
admin.site.register(Place)
# Register your models here.
