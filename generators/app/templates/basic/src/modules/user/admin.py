from django.contrib import admin 
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

# Register your models here.
from .models.user import User as usermodel

class CustomUserAdmin(BaseUserAdmin): 
  fieldsets = ( 
      (_('Login Details'), {'fields': ('email', 'password', )}), 
      (_('Personal info'), {'fields': ('first_name', 'last_name','gender','phone_no',)}),   
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}), 
  ) 
  #'user_permissions'
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone_no"] 
  search_fields = ('email', 'first_name', 'last_name') 
  ordering = ('first_name', ) 



admin.site.register(usermodel,CustomUserAdmin)