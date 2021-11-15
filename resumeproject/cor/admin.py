from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','age','con','add','state','city','zip','post','skill','ho1','ho2','ho3']