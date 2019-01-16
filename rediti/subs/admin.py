from django.contrib import admin
from .models import Subred, Thread, Post, Subscription


class SubredAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'creator']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Subred, SubredAdmin)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Subscription)