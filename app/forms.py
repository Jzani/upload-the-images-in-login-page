from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='User Name')
    address = forms.CharField(max_length=255, label='Address')
    profile_pic = forms.ImageField(label='Profile Picture')