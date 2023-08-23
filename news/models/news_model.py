from django.db import models
from .user_model import Users
from validators import validate_composite_title


class News(models.Model):
    title = models.CharField(
        max_length=200, blank=False, null=False,
        validators=[validate_composite_title,]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news/static/img/", null=False, blank=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
