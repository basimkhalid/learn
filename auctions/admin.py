from django.contrib import admin
from .models import *

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title","description","imageurl","author","listdate","initialprice","bidinprogress")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","listing","commentuser","comment","commentdate")

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment, CommentAdmin)
