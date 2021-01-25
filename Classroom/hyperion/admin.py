from django.contrib import admin

# Register your models here.
from .models import user,user_login,content

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ['ID','FirstName','LastName','Email']


@admin.register(user_login)
class userAdmin(admin.ModelAdmin):
    list_display = ['User_ID','Password']



@admin.register(content)
class userAdmin(admin.ModelAdmin):
    list_display = ['ID','Attachment']