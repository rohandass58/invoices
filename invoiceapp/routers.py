from rest_framework.routers import DefaultRouter

from .viewsets import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()

router.register(r"invoice", InvoiceViewSet, basename="invoice")
router.register(r"invoice_detail", InvoiceDetailViewSet, basename="invoice_detail")
