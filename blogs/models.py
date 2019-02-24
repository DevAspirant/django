from django.db import models

# Create your models here.
class blogs(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=15,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __unicode__(self):
        return self
