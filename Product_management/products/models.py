from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Explicitly define product_id as the primary key
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name