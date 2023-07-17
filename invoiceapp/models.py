from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    date = models.DateField(
        default=timezone.now,
        blank=True,
        null=True,
    )
    invoice_number = models.AutoField(
        primary_key=True,
    )
    customer_name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return str(self.invoice_number) + " " + self.customer_name


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="invoice_details",
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    quantity = models.IntegerField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            f"Invoice: {self.invoice.invoice_number}, Description: {self.description}"
        )

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
