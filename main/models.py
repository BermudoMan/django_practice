from django.db import models

class GalleryItem(models.Model):
    title = models.CharField('title', max_length=150)
    way = models.TextField('way')
    text = models.TextField('some_info')

    def __str__(self):
        return self.title


