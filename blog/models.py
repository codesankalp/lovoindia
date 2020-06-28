from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaulttags import register

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})


	@register.filter
	def get_image(self):
		return self.author.social_auth.get().extra_data['picture']