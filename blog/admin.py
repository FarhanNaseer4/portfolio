from django.contrib import admin
from .models import BlogPost, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]

admin.site.register(BlogPost, BlogAdmin)
# admin.site.register(Tag)