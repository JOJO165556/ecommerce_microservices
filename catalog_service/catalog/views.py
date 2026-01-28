from django.http import JsonResponse
from .models import Product

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        return JsonResponse(product.to_dict())
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)