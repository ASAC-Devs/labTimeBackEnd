from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.base import Model


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)


    def create_user(self, email, user_name, first_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        ordering = ('email',)

        user.set_password(password)
        user.save()
        return user
   

class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    password =models.CharField(max_length=255)
    last_login=models.DateField(default=False)
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

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','role' ,'course']

    def __str__(self):
        return self.user_name