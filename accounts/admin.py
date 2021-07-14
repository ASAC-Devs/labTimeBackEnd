from django.contrib import admin
from accounts.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Profile
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('role','course')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name','password1', 'password2', 'first_name','last_name', 'is_active', 'is_staff')}
         ),
    )
admin.site.register(Profile, UserAdminConfig)