from django.contrib import admin

from .models import Articles, Article_Categorys, Categorys, Article_Tags, Tags, User_Views, Comments

admin.site.register(Articles)
admin.site.register(Article_Categorys)
admin.site.register(Categorys)
admin.site.register(Article_Tags)
admin.site.register(Tags)
admin.site.register(User_Views)
admin.site.register(Comments)