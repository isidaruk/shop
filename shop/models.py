from django.db import models


from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """docstring for Category
    Products are organized into different categories.
    """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # Retrieve the URL for a given object.
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    """docstring for Product
    The catalog of our shop will consist of products.
    """
    name = models.CharField(max_length=200, db_index=True)

    # The slug for this product to build beatiful URLs.
    slug = models.SlugField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name='In stock')
    avaliable = models.BooleanField(default=True,
                                    verbose_name='Avaliable now')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Many-to-one relationship.
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
