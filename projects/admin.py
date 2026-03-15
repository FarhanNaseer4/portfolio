from django.contrib import admin

# Register your models here.
from .models import Project, ProjectImage, Tag

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)