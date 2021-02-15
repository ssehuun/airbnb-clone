from django.contrib import admin
from . import models  # admin.py와 같은 위치에 있는 모델을 불러옴

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
