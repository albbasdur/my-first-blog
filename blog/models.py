from django.db import models
from django.utils import timezone

# Create your models here.
# Define all the objects.
# This is the place where we will define the blog entry point
# 20200307_ABD
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # Long text with no limit:
    text = models.TextField()
    # Date time field
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title