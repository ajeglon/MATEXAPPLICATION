from django.db import models

# Create your models here.
class CertHolder(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()
    def __str__(self):
        return self.fname + ' ' + self.lname
