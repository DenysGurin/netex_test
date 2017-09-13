from django.db import models
from django.urls import reverse

def directory_path(instance, filename):
   
    return '{0}/{1}'.format(instance.id, filename)


class Tire(models.Model):

    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    diameter = models.PositiveIntegerField(null=True, blank=True)
    speed_index = models.PositiveIntegerField(null=True, blank=True)
    picture = models.FileField(upload_to=directory_path, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('tire-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s"%(self.id)
