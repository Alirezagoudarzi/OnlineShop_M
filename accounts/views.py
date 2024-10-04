from django.shortcuts import render,redirect
import random
from django.views import View
from django.contrib import messages

#locals
from .forms import UserRegistrationForm,VerifyCodeForm
from .models import OtpCode,User
from utils import send_otp_code


# Create your views here.
class UserRegisterView(View):

    form_class=UserRegistrationForm

    def get(self,request):
        form=self.form_class()
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            random_code=random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'],random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'],code=random_code)
            request.session['user_registration_info']={
                'phone_number':form.cleaned_data['phone'],
                'full_name':form.cleaned_data['full_name'],
                'email':form.cleaned_data['email'],
                'password':form.cleaned_data['password']
            }
            messages.success(request,'OtpCode send. please check your phone.')
            return redirect('accounts:verify_code')
        return render(request,'accounts/register.html',{'form':form})
    


class UserRegisterVerifyCode(View):
    
    form_class=VerifyCodeForm

    def get(self,request):
        form=self.form_class()
        return render(request,'accounts/verify.html',{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user_session=request.session['user_registration_info']
            otp_code_instance=OtpCode.objects.get(phone_number=user_session['phone_number'])
            if otp_code_instance.code ==form.cleaned_data['code']:
                User.objects.create_user(
                    email=user_session['email'],
                    phone_number=user_session['phone_number'],
                    full_name=user_session['full_name'],
                    password=user_session['password']
                )
                otp_code_instance.delete()
                messages.success(request,'you registered successfully','success')
                return redirect('home:home')
            else:
                messages.error(request,'wrong code','danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')


            
