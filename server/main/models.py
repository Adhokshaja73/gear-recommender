from django.db import models

# Create your models here.
class Videos(models.Model):
    video = models.FileField(upload_to="")
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title