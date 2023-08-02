from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, "index.html")


def invoice_details_page(request):
    return render(request, "invoice_details.html")


def invoices(request):
    return render(request, "invoices.html")


def specific_invoice(request, pk):
    invoice = InvoiceDetail.objects.filter(pk=pk)
    context = {'invoice': invoice}
    return render(request, 'specific_invoice.html', context)
