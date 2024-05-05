from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

class Product(models.Model):
    pass


class File(models.Model):
    pass