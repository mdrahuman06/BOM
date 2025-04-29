from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BOMItem(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kg'),
        ('nos', 'Nos'),
        ('time', 'Time (hr/min)'),
    ]

    TYPE_CHOICES = [
        ('material', 'Material'),
        ('labour', 'Labour'),
        ('other', 'Other'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bom_items')
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    item_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    notes = models.TextField(blank=True)

    custom_item_type = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return f"{self.item_name} ({self.get_item_type_display()})"
