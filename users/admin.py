from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # admin.py와 같은 위치에 있는 모델을 불러옴

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
