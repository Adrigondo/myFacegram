#Django
from django import forms

from django.contrib.auth.models import User
from users.models import Profile

from django.contrib.auth import authenticate, login

class UpdateProfileForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(),required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    phone_number=forms.CharField(max_length=20, required=True)
    birthday=forms.IntegerField(required=True)
    birthmonth=forms.IntegerField(required=True)
    birthyear=forms.IntegerField(required=True)
    description=forms.CharField(max_length=500, required=True)
    picture=forms.ImageField(required=False)

    def save(self, user, profile):
        data=self.cleaned_data
        user.first_name=data["first_name"]
        user.last_name=data["last_name"]
        user.email=data["email"]
        user.save()
        profile.phone_number=data["phone_number"]
        profile.birthday=data["birthday"]
        profile.birthmonth=data["birthmonth"]
        profile.birthyear=data["birthyear"]
        profile.description=data["description"]
        if data["picture"]:
            profile.picture=data["picture"]
        profile.save()

class SignupForm(forms.Form):
    username= forms.CharField(min_length=4, max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())
    password_confirmation=forms.CharField(widget=forms.PasswordInput())

    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.CharField(widget=forms.EmailInput())
    
    def clean(self):
        data=super().clean()
        password=data['password']
        username=data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already in use.")
        password_confirmation=data['password_confirmation']
        if password!=password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return data
    
    def save(self, request):
        data=self.cleaned_data
        data.pop("password_confirmation")

        user=User.objects.create_user(**data)
        user.save()
        profile=Profile(user=user)
        profile.save()
        login(request, user)

class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)
    
    def clean(self):
        data=super().clean()
        username=data['username']
        password=data['password']

        user_exists=User.objects.filter(username=username).exists()
        user=authenticate(self, username=username, password=password)
        
        #Validate if user exists
        if not user_exists:
            raise forms.ValidationError("User does not exist")
        #Validate if user is authenticate
        if not user:
            raise forms.ValidationError('The username or password is incorrect')
        return data

    def save(self, request):
        data=self.cleaned_data
        username=data['username']
        password=data['password']
        user=authenticate(self, username=username, password=password)
        login(request, user)