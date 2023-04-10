from django.contrib import admin
from .models import Category,Expense,Budget,History,UserProfile
# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(History)
admin.site.register(UserProfile)