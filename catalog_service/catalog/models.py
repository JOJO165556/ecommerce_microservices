from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": str(self.price), "stock": self.stock}