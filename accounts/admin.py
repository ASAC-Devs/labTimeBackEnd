from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name','is_staff', 'get_location','get_course')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.role
    get_location.short_description = 'role'

    def get_course(self, instance):
        return instance.profile.course
    get_course.short_description = 'course'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

# from django.contrib import admin
# from .models import NewUser
# from django.contrib.auth.admin import UserAdmin
# from django.forms import TextInput, Textarea, CharField
# from django import forms
# from django.db import models



# class UserAdminConfig(UserAdmin):
#     model = NewUser
#     search_fields = ('email', 'user_name', 'first_name',)
#     list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
#     ordering = ('-start_date',)
#     list_display = ('email', 'user_name', 'first_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email', 'user_name', 'first_name',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('about',)}),
#     )
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )


# admin.site.register(NewUser, UserAdminConfig)