from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from members.models import Member
import os
import datetime


def get_image_path(instance, filename):
    return 'blog/' + filename.split('/')[-1]


class Post(models.Model):
    title = models.CharField('Título', max_length=255)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, editable=False, null=True)
    text_call = models.CharField('Descrição', max_length=255)
    text_content = models.TextField('Conteúdo', )
    thumbnail = models.ImageField('Thumbnail', upload_to=get_image_path)
    publish_date = models.DateField(auto_now=False, auto_now_add=True)
    last_modification = models.DateField(auto_now=True, auto_now_add=False)
    publish_as_team = models.BooleanField('Postar em nome da equipe', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
