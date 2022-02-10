from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name=' عنوان دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return f"/products/{self.title.replace(' ', '-')}"


    def __str__(self):
        return self.title
