from django.contrib import admin
from Insta.models import Post, InstaUser, UserConnection, Like, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(UserConnection)
admin.site.register(Like)
admin.site.register(Comment)