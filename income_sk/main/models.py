

# Create your models here.
from django.db import models


class fragmentname(models.Model):
    identifier = models.CharField(max_length = 100 ,  null=True)
    name = models.CharField(max_length = 250, null = True)

  
   

    def __str__(self):
        return self.name

class mall(models.Model):
    name = models.ForeignKey(fragmentname, on_delete=models.CASCADE)
    img1 = models.CharField(max_length = 250, default = 'NULL')
    img2 = models.CharField(max_length = 250, default = 'NULL')
    img3 = models.CharField(max_length = 250, default = 'NULL')
    knowmore = models.CharField(max_length = 1000, default = 'NULL')


    def __str__(self):
        return "hi"


class codingninja(models.Model):
    name = models.ForeignKey(fragmentname, on_delete=models.CASCADE)
    img1 = models.CharField(max_length = 250, default = 'NULL', null = True )
    img2 = models.CharField(max_length = 250, default = 'NULL', null = True)
    img3 = models.CharField(max_length = 250, default = 'NULL', null = True)
    knowmore = models.CharField(max_length = 1000, default = 'NULL' , null = True)


    def __str__(self):
        return "hi"