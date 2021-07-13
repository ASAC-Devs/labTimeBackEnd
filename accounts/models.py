from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model


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

    

