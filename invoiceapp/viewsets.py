from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .models import Invoice, InvoiceDetail


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        invoice_serializer = self.get_serializer(data=request.data)
        if invoice_serializer.is_valid():
            invoice = invoice_serializer.save()
            invoice_details_data = request.data.get("invoice_details", [])
            invoice_details_serializer = InvoiceDetailSerializer(
                data=invoice_details_data, many=True
            )
            if invoice_details_serializer.is_valid():
                invoice_details_serializer.save(invoice=invoice)
                return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
