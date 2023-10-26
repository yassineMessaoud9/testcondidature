from django.db import models

# Create your models here.

class Annotation(models.Model):
    label = models.CharField(max_length=255)
    start = models.IntegerField(null=True, blank=True)
    end = models.IntegerField(null=True, blank=True)
    text = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return str(self.label)
    
class Documents(models.Model):
    document = models.CharField(max_length=4055)
    annotation = models.ManyToManyField(Annotation, blank=True)


    def __str__(self):
        return str(self.document)