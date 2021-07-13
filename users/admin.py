from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ["first_name", "last_name", "email"]
    ordering = ("email",)


admin.site.register(User, UserAdmin)

