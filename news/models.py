from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('youth', 'Youth'),
        ('lessons', 'Lessons'),
        ('events', 'Events'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=200, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=100, blank=True)
    date_taken = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date_taken']
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title
