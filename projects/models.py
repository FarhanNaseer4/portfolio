from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    image = models.ImageField(upload_to="projects/")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    category = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True) 
    records_scraped = models.IntegerField(default=0)
    uptime = models.CharField(max_length=50, blank=True)
    speed = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return f"Image for {self.project.title}"