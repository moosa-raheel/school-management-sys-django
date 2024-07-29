from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

# Ye Signup form he
class Registration_form(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off"}),label="Enter Password")
    password2 = forms.CharField(widget=forms.TextInput(attrs={"autocomplete":"off"}),label="Enter Password Again")
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email"]
        widgets = {"first_name": forms.TextInput({"autocomplete":"off"}),"last_name":forms.TextInput(attrs={"autocomplete":"off"}),"username":forms.TextInput(attrs={"autocomplete":"off"}),"email":forms.EmailInput(attrs={"autocomplete":"off"})}
        labels = {"first_name":"Enter First Name","last_name":"Enter Last Name","email":"Enter Email","username":"Enter Username"}
        
# Ye Loign Form he 
class Login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","autocomplete":"off"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))