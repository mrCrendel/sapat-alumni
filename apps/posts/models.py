from ckeditor.fields import RichTextField
from django.db import models

from apps.commons.helpers import generate_filename
from apps.commons.models import TimestampAbstractModel


class PostCategory(TimestampAbstractModel):
    """
        Post category model
    """
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(
        verbose_name='Название', max_length=255
    )

    def __str__(self):
        return self.title


class Post(TimestampAbstractModel):
    """
        Post model
    """
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE,
        verbose_name='Категоря', related_name='posts'
    )
    title = models.CharField(
        verbose_name='Название', max_length=255
    )
    description = RichTextField(verbose_name='Описание')
    image = models.FileField(verbose_name='Картинка', upload_to=generate_filename)

    def __str__(self):
        return self.title
