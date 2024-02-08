from django.db import models

# Create your models here.
from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')

    link = models.URLField(blank=True)
    technology = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return self.title




