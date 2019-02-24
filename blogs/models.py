from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=15,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)
    # the list of shown into Signup admin Page 
    def __unicode__(self):
        return self.email
        
