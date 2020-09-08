from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='cover/', blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)
