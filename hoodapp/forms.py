from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Hood,Business,Post

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pro_photo','email','neighbourhood','bio')


class NeighbourForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name','image','location','occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude =  []
        fields = ['name','description','email','neighbourhood']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =  ['user','neighbourhood']
        fields = ['post']