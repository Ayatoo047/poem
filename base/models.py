from django.db import models
import uuid

# Create your models here.
class Poems(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key = True, unique = True, editable=False)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    index = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['index']

class Message(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key = True, unique = True, editable=False)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['is_read', 'created']


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)


class Reviews(models.Model):
    # owner = 
    
    description =  models.TextField(null=True, blank=True)

