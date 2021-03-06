from io import StringIO
from django.db import models
from django.http.response import StreamingHttpResponse

# Create your models here.
class Feedback(models.Model):

    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

   