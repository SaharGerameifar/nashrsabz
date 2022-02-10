from django.contrib.auth.models import User
from django.db.models import Q
from django.db import models
import uuid
import os
from e_shop_products_category.models import ProductCategory
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class ProductManager(models.Manager):

    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        query_set = self.get_active_product().filter(id=product_id)
        if query_set.count() == 1:
            return query_set.first()
        else:
            return None

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(short_description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__title__iexact=category_name, active=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان کتاب')
    author = models.CharField(max_length=150, verbose_name='نویسنده کتاب', null=True)
    translator = models.CharField(max_length=150, verbose_name='مترجم کتاب', null=True)
    published = models.CharField(max_length=150, verbose_name='نوبت چاپ', null=True)
    publication_date = models.CharField(max_length=150, verbose_name='تاریخ چاپ', null=True)
    product_Code = models.UUIDField(default=uuid.uuid4, primary_key=False, editable=False, verbose_name='کد کتاب ')
    short_description = models.TextField(verbose_name='توضیحات کوتاه', null=True)
    isbn_book = models.CharField(max_length=150, verbose_name='شابک کتاب ', null=True)
    book_genre = models.CharField(max_length=150, verbose_name='ژانر کتاب', null=True)
    ghate_book = models.CharField(max_length=150, verbose_name='قطع', null=True)
    jeld_book = models.CharField(max_length=150, verbose_name='جلد', null=True)
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(verbose_name='تصویر', null=True, blank=True, upload_to=upload_image_path)
    active = models.BooleanField(verbose_name='فعال/غیر فعال', default=False)
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    likes = models.ManyToManyField(User, related_name='product_like', blank=True)
    comments = GenericRelation(Comment)
    objects = ProductManager()

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"

    def __str__(self):
        return self.title


class ProductGalley(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(verbose_name='تصویر', upload_to=upload_gallery_image_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name_plural = 'تصاویر'
        verbose_name = 'تصویر'

    def __str__(self):
        return self.title




