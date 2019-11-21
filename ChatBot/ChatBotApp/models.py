from django.db import models
class Odpowiedz(models.Model):
    bocik= models.TextField()
    zdjecie=models.ImageField()

    def publish(self):
        self.save()

# Create your models here.
