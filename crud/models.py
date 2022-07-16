from django.db import models
from django.template.defaultfilters import truncatechars

# Create your models here.

class Image(models.Model):
    ImgName = models.CharField(max_length=50, blank=False)
    # ImgURL = models.ImageField(upload_to='images/', blank=True)
    ImgURL = models.URLField(blank=False)
    ImgDetails = models.TextField(default=None, max_length=1500, blank=False)

    @property
    def short_description(self):
        return truncatechars(self.ImgDetails, 100)