

# Create your models here.
from django.db import models


class fragmentname(models.Model):
    identifier = models.CharField(max_length = 100 ,  null=True , default = 1234)
    name = models.CharField(max_length = 250, null = True)


  
   

    def __str__(self):
        return self.identifier

class organisations(models.Model):
    name = models.CharField(max_length = 250, default = 'NULL')
    img1 = models.CharField(max_length = 250, default = 'NULL')
    img2 = models.CharField(max_length = 250, default = 'NULL')
    img3 = models.CharField(max_length = 250, default = 'NULL')
    description = models.CharField(max_length = 250, default = 'NULL')
    knowmore = models.CharField(max_length = 1000, default = 'NULL')


    def __str__(self):
        return self.name

