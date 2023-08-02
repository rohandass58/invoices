from django.urls import path, include
from .routers import router
from . import views

urlpatterns = [
    path("invoices/", include(router.urls)),
    path("", views.home, name="home"),
    path("invoice_details/", views.invoice_details_page, name="invoice_details_page"),
    path("invoice_details/list/", views.invoices, name="invoices"),
    path("specific_invoice/<int:pk>/", views.specific_invoice, name="specific_invoice"),
]
