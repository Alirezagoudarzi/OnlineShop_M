from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#locals
from .models import User


class UserCreationForm(forms.ModelForm):

    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','phone_number','full_name']

        #is_active= models.BooleanField(default=True)
        #is_admin=models.BooleanField(default=False) 


    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password must be match!')
        return cd['password2']
    

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    


class UserChangeForm(forms.ModelForm):

   #password=ReadOnlyPasswordHashField(help_text="hello dear, you can change password by using <a href=\"../password/\">this link</a>.")

    class Meta:
        model=User
        fields=['email','phone_number','full_name','password','last_login']







class UserRegistrationForm(forms.Form):
    email=forms.EmailField(label='      Email',required=True)
    full_name=forms.CharField(label='  Full Name', max_length=100, required=True)
    phone=forms.CharField(label='      Phone',max_length=11, required=True)
    password=forms.CharField(label='   Password',widget=forms.PasswordInput,required=True)