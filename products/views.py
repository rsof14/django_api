from django.shortcuts import redirect
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
        serializer = ProductSerializer()
        return Response({'serializer': serializer, 'products': ProductSerializer(products, many=True).data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'product': serializer.data})

        serializer.save()
        return redirect(request.path_info)




