from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


class ProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        return Response({'products': ProductSerializer(products, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'product': serializer.data})


