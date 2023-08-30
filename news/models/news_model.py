from django.db import models
from .category_model import Categories
from .user_model import Users
from news.validators import validate_composite_title, validate_date_format
from cloudinary.models import CloudinaryField # quando precisar colocar imagem tem que mudar as models
 


class News(models.Model):
    title = models.CharField(
        max_length=200, blank=False, null=False,
        validators=[validate_composite_title]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
    created_at = models.DateField(validators=[validate_date_format], null=False)
    image = models.ImageField(upload_to="img/", null=False, blank=True)
    # image = CloudinaryField(blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
