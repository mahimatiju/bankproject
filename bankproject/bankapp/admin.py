from django.contrib import admin
from .models import Detail


# Register your models here.
class UserDetail(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'district', 'branch', 'account',
                    'material']


admin.site.register(Detail,UserDetail)
