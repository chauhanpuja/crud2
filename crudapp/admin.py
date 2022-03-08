from django.contrib import admin
from . models import  User_Data
# Register your models here.

@admin.register(User_Data)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')