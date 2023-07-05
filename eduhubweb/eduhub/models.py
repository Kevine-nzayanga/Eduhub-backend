from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    image= models.ImageField()
    genre = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    











# cover_image = models.ImageField(upload_to='book_covers/')
# class Genre(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name

# Create your models here.
