from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from .models import Profile,Circle

class UserRegisterForm(UserCreationForm):

#Specifying a range of Datewidget years
    YEARS= [x for x in range(1940,2021)]
    email = forms.EmailField()
    # first_name = forms.CharField(max_length = 20)
    # birth_date = forms.DateField(label='What is your date of birth?', widget=forms.SelectDateWidget(years=YEARS))
  
    class Meta:
        model = User
        # fields = ['email','first_name','username','birth_date','password1','password2']
        fields = ['email','username','password1','password2']



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    about = forms.CharField(max_length=50)

    class Meta:
        model = Profile
        fields = ['image','about']        

class CircleUpdateForm(forms.ModelForm):

    class Meta:
        model = Circle
        fields = ['friends']

