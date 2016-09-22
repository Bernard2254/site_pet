from django.db import models
import os, datetime
from django.conf import settings
from django.contrib.auth.models import User


def get_image_path(instance, filename):
    if instance.id is not None:
        path = os.path.join(settings.MEDIA_ROOT, 'members/photos', str(instance.id))
        if os.path.isfile(path):
            os.remove(path)
        return os.path.join('members/photos', str(instance.id))
    return os.path.join('members/photos', datetime.datetime.now().strftime('%Y%m%d%H%M%S'), filename)


class Member(models.Model):
	MEMBER = 'MB'
	EX_MEMBER = 'EM'
	TUTOR = 'TT'
	VOLUNTARY = 'VT'
	STATUS_CHOICES = (
		(MEMBER, 'Membro'),
		(EX_MEMBER, 'Ex-Membro'),
		(TUTOR, 'Tutor'),
		(VOLUNTARY, 'Voluntário'),
	)
	name = models.CharField(max_length=255)
	photo = models.ImageField(upload_to=get_image_path)
	facebook_link = models.CharField(max_length=255, blank=True)
	lattes_link = models.CharField(max_length=255, blank=True)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	email = models.EmailField(max_length=255)
	status = models.CharField(
		max_length=2,
		choices=STATUS_CHOICES,
		default=MEMBER,
    )

	def __str__(self):
		return self.name


class MyMember(Member):
    class Meta:
        proxy = True
