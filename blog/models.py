from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Adjust 'blog:post_detail' to your URL pattern name
        return reverse('blog:post_detail', args=[self.id])

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = RichTextField(blank=True, null=True)
    event_date = models.DateTimeField()
    featured_image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title
