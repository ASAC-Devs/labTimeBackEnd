from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model
# from django import forms
# from django.utils import timezone
# from django.utils.translation import gettext_lazy
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class CustomAccountManager(BaseUserManager):
#     def create_user(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(gettext_lazy('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class NewUser(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(gettext_lazy('email address'), unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name', 'first_name']

#     def __str__(self):
#         return self.user_name



class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name='profile')
    
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)

    STUDENT = 'Student'
    TA = 'TA'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TA, 'TA'),
    )
    role = models.CharField(
        choices=ROLE_CHOICES, null=True, blank=True, max_length=10, help_text='Role')
    Code201 , Code301 ,Code401_python , Code401_java ,Code401_javaScript = 'code201' ,'code301' ,'code401_python' ,'code401_java','code401_javaScript'
    Courses_list=(
        (Code201 ,'code201'),
        (Code301 ,'code301'),
        (Code401_python ,'code401_python'),
        (Code401_java ,'code401_java'),
        (Code401_javaScript ,'code401_javaScript'),
    )
    course=models.CharField(
       choices=Courses_list, null=True, blank=True , max_length=256, help_text='Course')

    def __str__(self):
        return self.user.username

    class Meta:
        def __str__(self):
            pass

    

