from django.contrib import admin
from .models import BlogPost
from django.utils import timezone
from datetime import timedelta
from .models import GalleryImage

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'published_date', 'is_published_recently')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'published_date')
    actions = ['publish_selected', 'unpublish_selected']
    
    def is_published_recently(self, obj):
        return obj.published_date >= timezone.now() - timedelta(days=1)
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'
    
    def publish_selected(self, request, queryset):
        queryset.update(is_published=True)
    publish_selected.short_description = "Publish selected posts"
    
    def unpublish_selected(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_selected.short_description = "Unpublish selected posts"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_taken', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'caption')
    prepopulated_fields = {'caption': ('title',)}