from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name='Task')
    description =models.CharField(max_length=255,verbose_name='Description')
    cat = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    complete = models.BooleanField(default=False,verbose_name='Is complete')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.title