from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
import requests

app = FastAPI(title="API Gateway ecommerce")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CATALOG_URL = "http://catalog:8001/api/products/"
ORDER_URL = "http://order:8002/api/orders/create/" 

@app.get("/catalogue/{item_id}")
def get_product(item_id: int):
    # La Gateway redirige vers le Catalogue
    response = requests.get(f"{CATALOG_URL}{item_id}/")
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=404, detail="Produit non trouvé")

@app.post("/commander")
def place_order(product_id: int, quantity: int):
    # La Gateway redirige vers les Commandes
    data = {'product_id': product_id, 'quantity': quantity}
    response = requests.post(ORDER_URL, data=data)
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)