from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    OT = 0
    VH = 1
    ARTICLE_TOPICS = [
        (OT, 'Others'),
        (VH, 'Vehicle Related'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=250)
    content = models.TextField(max_length=600)
    topic = models.IntegerField(choices=ARTICLE_TOPICS, default=OT)
    posted_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_comment")
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="comments")
    comment = models.TextField(max_length= 256)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.article.pk})

    class Meta:
        ordering = ['-comment_date',]