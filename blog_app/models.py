from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    author=models.ForeignKey("auth.user", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True, blank=True)

    def __str__(self):
     return self.title
