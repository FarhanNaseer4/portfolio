from django.db import models
# Correct way for Django
from django.utils.text import slugify
from projects.models import Tag
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/")
    published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class BlogImage(models.Model):
    blog = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='gallery',
        db_column='post_id'   # tells Django to use the existing column
    )
    image = models.ImageField(upload_to='blog/gallery/')

    def __str__(self):
        return f"Image for {self.blog.title}"