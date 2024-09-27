from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Product
from .serializers import ProductSerializer


class ProductsAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        products = Product.objects.all()
        return Response(
            data={'products': ProductSerializer(products, many=True).data},
            status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data={'product': serializer.data},
                            status=status.HTTP_201_CREATED)
        except ValidationError:
            return JsonResponse({
                'message': 'Название продукта должно быть уникальным'},
                status=status.HTTP_400_BAD_REQUEST)
