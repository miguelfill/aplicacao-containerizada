from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud
from app.models import models
from app.models.database import get_db

app = FastAPI()

# Endpoint para listar clientes
@app.get("/clients")
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_clients(db, skip=skip, limit=limit)

# Endpoint para criar um novo cliente
@app.post("/clients")
def create_client(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_client(db, name=name, email=email)

# Endpoint para listar ativos
@app.get("/assets")
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_assets(db, skip=skip, limit=limit)

# Endpoint para criar um novo ativo
@app.post("/assets")
def create_asset(ticker: str, name: str, price: float, db: Session = Depends(get_db)):
    return crud.create_asset(db, ticker=ticker, name=name, price=price)

# Endpoint para listar alocações de um cliente
@app.get("/clients/{client_id}/allocations")
def get_allocations(client_id: int, db: Session = Depends(get_db)):
    return crud.get_allocations_by_client(db, client_id=client_id)

# Endpoint para criar uma nova alocação
@app.post("/allocations")
def create_allocation(client_id: int, asset_id: int, quantity: float, price_at_purchase: float, db: Session = Depends(get_db)):
    return crud.create_allocation(db, client_id=client_id, asset_id=asset_id, quantity=quantity, price_at_purchase=price_at_purchase)
