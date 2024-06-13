from django.db import models
from django.urls import reverse

class Build(models.Model):
	title = models.CharField(max_length=255, verbose_name = 'Заголовок')
	content = models.TextField(blank=True, verbose_name = 'Краткое содержание')
	photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name = 'Фото 33%')
	photoTi = models.ImageField(upload_to="photosTi/%Y/%m/%d", verbose_name = 'Фото 100%')
	video = models.TextField(blank=True, null=True, verbose_name = 'Видео')
	time_create = models.DateTimeField(auto_now_add=True,  verbose_name = 'Время публикации')

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
			return reverse("post", kwargs={"post_id": self.pk})
	class Meta:
		verbose_name = 'Ремонт'
		verbose_name_plural = 'Ремонт'
		ordering = ['-time_create']
	
class Sale(models.Model):
	title = models.CharField(max_length=255, verbose_name = 'Заголовок')
	content = models.TextField(blank=True, verbose_name = 'Краткое содержание')
	photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name = 'Фото 33%')
	time_create = models.DateTimeField(auto_now_add=True,  verbose_name = 'Время публикации')
	
	class Meta:
		verbose_name = 'Акции'
		verbose_name_plural = 'Акции'
		ordering = ['-time_create']
	def __str__(self):
		return self.title