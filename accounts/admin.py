from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#locals
from .forms import UserChangeForm,UserCreationForm
from .models import User,OtpCode


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    fieldsets=(
        ('main',{'fields':('email','phone_number','full_name','password')}),
        ('permision',{'fields':('is_active','is_admin','last_login')}),
    )

    add_fieldsets=(
        ('new user',{'fields':('email','phone_number','full_name','password1','password2')}),
    )


    list_display=('email','phone_number','full_name','is_admin')
    list_filter=('is_admin',)
    search_fields=('email','full_name')
    ordering=('is_admin',)
    filter_horizontal=()

#---------------------------------
@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display=('phone_number','code','created')

#---------------------------------
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
