from django.db import models


class Culture(models.Model):
    country = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='culture_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.country} - {self.title}"
