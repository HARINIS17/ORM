from django.db import models
from django.contrib import admin
class Movie(models.Model):
    
    name=models.CharField(max_length=100)
    actor=models.CharField()
    year=models.IntegerField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('name','actor','year')


