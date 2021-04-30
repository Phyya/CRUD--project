from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fullPost', kwargs={"pk": self.id})


class Comment(models.Model):

    post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE,)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return 'By: %s -%s' %(self.post.name, self.body)

    