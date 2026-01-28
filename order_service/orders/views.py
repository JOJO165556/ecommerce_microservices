from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from .models import Order

@csrf_exempt 
def create_order(request):
    if request.method == 'POST':
        p_id = request.POST.get('product_id')
        qty = int(request.POST.get('quantity', 1))

        # Appel au service Catalogue (Port 8001)
        try:
            response = requests.get(f'http://catalog:8001/api/products/{p_id}/')            
            if response.status_code == 200:
                product_data = response.json()
                total = float(product_data['price']) * qty
                
                # Sauvegarde dans la base de données du service ORDER
                order = Order.objects.create(product_id=p_id, quantity=qty, total_price=total)
                return JsonResponse({'order_id': order.id, 'status': 'Success', 'total': total})
            else:
                return JsonResponse({'error': 'Produit non trouvé dans le catalogue'}, status=404)
        except requests.exceptions.ConnectionError:
            return JsonResponse({'error': 'Service Catalogue indisponible'}, status=503)

    return JsonResponse({'error': 'Seul le POST est autorisé'}, status=405)