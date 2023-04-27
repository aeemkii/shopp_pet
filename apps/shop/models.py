from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField("Название", max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField('Описание')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete= models.SET_NULL, 
         null=True, )
    is_available = models.BooleanField("Доступно", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField("Изображение", upload_to="product/images/", null=True)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name