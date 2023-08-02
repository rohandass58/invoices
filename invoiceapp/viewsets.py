from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .models import Invoice, InvoiceDetail


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def perform_create(self, serializer):
        # Save the invoice and return the created instance
        instance = serializer.save()
        return instance

    @action(detail=True, methods=["post"])
    def add_invoice_details(self, request, pk=None):
        invoice = self.get_object()
        invoice_details_data = request.data.get("invoice_details", [])
        invoice_details_serializer = InvoiceDetailSerializer(data=invoice_details_data, many=True)
        if invoice_details_serializer.is_valid():
            invoice_details_serializer.save(invoice=invoice)
            return Response(invoice_details_serializer.data, status=status.HTTP_201_CREATED)
        return Response(invoice_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

    @action(detail=False, methods=["post"])
    def create_invoice_detail(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
