from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .viewsets import InvoiceViewSet, InvoiceDetailViewSet
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        # Set up the API request factory
        self.factory = APIRequestFactory()

    def test_create_invoice(self):
        data = {
            "customer_name": "John Doe",
            "date": "2023-08-02",
            # Add other required fields as needed
        }
        request = self.factory.post('/invoices/invoice/', data, format='json')
        view = InvoiceViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_create_invoice_detail(self):
        invoice = Invoice.objects.create(customer_name="John Doe", date="2023-08-02")
        data = {
            "invoice": invoice.pk,
            "description": "Item 1",
            "quantity": 2,
            "unit_price": 10.0,
            "price": 20.0,
        }
        request = self.factory.post('/invoice_details/', data, format='json')
        view = InvoiceDetailViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)

 
    def test_add_invoice_details(self):
        invoice = Invoice.objects.create(customer_name="John Doe", date="2023-08-02")
        data = {
            "invoice_details": [
                {
                    "description": "jhhgh",
                    "quantity": 45,
                    "unit_price": "988.00",
                    "price": "44460.00",
                    "invoice": invoice.pk,
                },
                {
                    "description": "tomato",
                    "quantity": 1,
                    "unit_price": "200.00",
                    "price": "200.00",
                    "invoice": invoice.pk,
                }
            ]
        }
        request = self.factory.post(f'/invoices/{invoice.pk}/add_invoice_details/', data, format='json')
        view = InvoiceViewSet.as_view({'post': 'add_invoice_details'})
        response = view(request, pk=invoice.pk)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 2)
