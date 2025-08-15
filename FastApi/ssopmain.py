from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Lista para almacenar productos en memoria
products = []

# Modelo para creación de productos
class Product(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    drop: int
    size: str
    color: str
    category: str
    stock: bool
    price: float

# Modelo para actualización de productos
class ProductUpdate(BaseModel):
    title: str
    overview: str
    drop: int
    size: str
    color: str
    category: str
    stock: bool
    price: float


# Creo un producto
@app.post('/products', tags=['Products'])
def create_product(product: Product):
    # Si no hay ID, asigna el siguiente disponible.
    if product.id is None:
        product.id = len(products) + 1
    products.append(product.model_dump())  # usar dict() si estás en Pydantic v1 != model_dum Pydantic v2
    return {"message": "Producto creado", "data": product}


# Obtengo todos los productos
@app.get('/products', tags=['Products'])
def obtain_products():
    return products


# Actualizo un producto por ID
@app.put('/product/{id}', tags=['Products'])
def update_product(id: int, product_data: ProductUpdate):
    for p in products:
        if p["id"] == id:
            p["title"] = product_data.title
            p["overview"] = product_data.overview
            p["drop"] = product_data.drop
            p["size"] = product_data.size
            p["color"] = product_data.color
            p["category"] = product_data.category
            p["stock"] = product_data.stock
            p["price"] = product_data.price
            return {"message": "Producto actualizado", "data": p}
    return {"error": "Producto no encontrado."}
