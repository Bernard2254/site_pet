from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from members.models import Member
from utils.upload_helper import get_image_path
import os
import datetime


class Post(models.Model):
    title = models.CharField('Título', max_length=255)
    author = models.ForeignKey(Member, on_delete=models.PROTECT, null=True, verbose_name='Autor')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, editable=False)
    text_call = models.CharField('Descrição', max_length=255)
    text_content = models.TextField('Conteúdo', )
    thumbnail = models.ImageField('Thumbnail', upload_to=get_image_path)
    publish_date = models.DateField(auto_now=False, auto_now_add=True)
    last_modification = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts (todos)'


class MyPost(Post):
    class Meta:
        proxy = True
        verbose_name = 'Post'
