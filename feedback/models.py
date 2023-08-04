from django.db import models


# Create your models here.
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.email
