from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
UserAdmin.fieldsets[1][1]['fields']=(
                        "first_name",
                        "last_name",
                        "email",
                        "description",
                        "profile",
                        "github",
                        "telegram",
                        "instagram",
                        "twitter",
                        )
UserAdmin.fieldsets[2][1]['fields']= (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "is_auther",
                        "is_team",
                        "groups",
                        "user_permissions",
                    ),


admin.site.register(User,UserAdmin)