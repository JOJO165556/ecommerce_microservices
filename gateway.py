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
    try:
        response = requests.get(f"{CATALOG_URL}{item_id}/", timeout=2) # Timeout pour éviter de bloquer
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Le service Catalogue est indisponible")

@app.post("/commander")
def place_order(product_id: int, quantity: int):
    try:
        data = {'product_id': product_id, 'quantity': quantity}
        response = requests.post(ORDER_URL, data=data, timeout=5)
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Le service Commande est indisponible")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)