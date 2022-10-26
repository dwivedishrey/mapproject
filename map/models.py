from django.db import models
class Search(models.Model):
    address=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    destination=models.CharField(max_length=200,null=True)
    ip=models.TextField(default=" ")
    def _str_(self):
        return self.address
# Create your models here
