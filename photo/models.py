from django.db import models


# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='photo/%Y%m%d')
    created = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '照片管理'
        db_table = 'tb_image'

    def __str__(self):
        return self.image.name
