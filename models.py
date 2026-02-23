from django.db import models
class Complaint(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
    def _str_(self):
        return self.title
# Create your models here