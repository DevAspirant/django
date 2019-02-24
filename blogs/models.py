from django.db import models

# Create your models here.
class blogs(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=15)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField()

    def __unicode__(self):
        return self
