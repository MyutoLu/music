from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = '我的音乐后台管理'
admin.site.site_header = '我的音乐'

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['label_id', 'label_name']
    search_fields = ['label_name']
    ordering = ['label_id']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_id', 'song_name', 'song_singer','song_album',
                    'song_release']
    search_fields = ['song_name', 'song_singer', 'song_album']
    ordering = ['song_id']
    list_filter = ['song_singer', 'song_album']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'comment_content', 'comment_user',
                    'song', 'comment_date' ]
    search_fields = ['comment_user', 'song', 'comment_date']
    list_filter = ['song', 'comment_date']
    ordering = ['comment_id']

@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ['dynamic_id', 'song', 'dynamic_plays', 'dynamic_search',
                    'dynamic_down']
    search_fields = ['song']
    list_filter = ['dynamic_plays', 'dynamic_search', 'dynamic_down']
    ordering = ['dynamic_id']