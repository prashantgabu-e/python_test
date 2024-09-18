from django.db.models import Sum, Count
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=["GET"], url_path="stats", detail=False)
    def stats(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise ValidationError("No products found")
        aggregated_qs = queryset.aggregate(total_amount=Sum('price'), total_products=Count('id'))
        response = {
            "total_amount": aggregated_qs.get('total_amount'),
            "total_products": aggregated_qs.get('total_products'),
        }
        return Response(response)
