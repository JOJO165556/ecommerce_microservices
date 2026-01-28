from django.db import models

class Order(models.Model):
    product_id = models.IntegerField() # On stocke l'ID, pas une ForeignKey !
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")