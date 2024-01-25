from django.db import models

# Create your models here.
class dropdown(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class cricket(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    
    class Meta:
        managed= False
        db_table = 'cricket'

class kabadi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        managed= False
        db_table = 'kabadi'
    
    
