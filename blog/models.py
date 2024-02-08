from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'publish'),
        ('dr', 'draft'),
    )
    images = models.ImageField(upload_to='blog/',null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    # tage
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    class Meta:
        ordering = ['created_date']  

    def __str__(self):
        return self.title


