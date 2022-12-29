from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# para empezar a definir lo que queremos dentro del proyecto


class Project(models.Model):

    # propiedades

    title = CharField(max_length=101)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)
