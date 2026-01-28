import requests

# 1. On vérifie le catalogue (Port 8001)
print("--- Test du Catalogue ---")
cat_req = requests.get('http://127.0.0.1:8001/api/products/1/')
print(f"Réponse Catalogue: {cat_req.json()}")

# 2. On tente de créer une commande (Port 8002)
# Ce service va appeler le port 8001 en interne
print("\n--- Test de la Commande ---")
data = {'product_id': 1, 'quantity': 2}
order_req = requests.post('http://127.0.0.1:8002/api/orders/create/', data=data)

if order_req.status_code == 200:
    print(f"Succès ! Commande créée : {order_req.json()}")
else:
    print(f"Échec : {order_req.text}")