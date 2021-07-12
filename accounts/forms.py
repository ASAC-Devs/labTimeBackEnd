from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from accounts.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=45, required=False)
    last_name = forms.CharField(
        max_length=45, required=False)
    email = forms.EmailField(
        max_length=254, help_text='Required. Provide a valid email address.')
    
    Code201 , Code301 ,Code401_python , Code401_java ,Code401_javaScript = 'code201' ,'code301' ,'code401_python' ,'code401_java','code401_javaScript'
    Courses_list=(
        (Code201 ,'code201'),
        (Code301 ,'code301'),
        (Code401_python ,'code401_python'),
        (Code401_java ,'code401_java'),
        (Code401_javaScript ,'code401_javaScript'),
    )
    course=forms.ChoiceField(
        choices=Courses_list,help_text='Course' )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'course')

class ProfileForm(forms.Form):
    enroll_number = forms.IntegerField(
        required=True, help_text='Required !!')

    STUDENT = 'Student'
    TA = 'TA'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TA, 'TA'),
    )

    def save(self, user_name):
        data = self.cleaned_data
        user = get_object_or_404(User, username=user_name)
        userProfile = Profile(user=user, enroll_number=data[
                              'enroll_number'], role='Student',)
        userProfile.save()