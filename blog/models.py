from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # tags = models.CharField(max_length=100, blank=True)
    # lnglat = models.CharField(max_length=50, blank=True, help_text='위도/경도 포맷으로 작성할것')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])
    # def __str__(self):
    #     return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
