from django.contrib import admin

# Register your models here.
from .models import InvoiceDetail, Invoice

admin.site.register(InvoiceDetail)
admin.site.register(Invoice)
