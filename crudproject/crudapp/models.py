from django.db import models

# Create your models here.
class Task(models.Model):
    slno=models.IntegerField()
    item_name=models.CharField(max_length=300)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.item_name