from django.db import models

class GalleryItem(models.Model):
    title = models.CharField('title', max_length=150)
    way = models.TextField('way')

    def __str__(self):
        return self.title