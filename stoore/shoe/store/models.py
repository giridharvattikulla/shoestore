from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"
