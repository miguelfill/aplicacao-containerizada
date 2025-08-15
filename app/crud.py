from sqlalchemy.orm import Session
from app.models import models

# ========================================
# Funções de CRUD para Clientes
# ========================================

# Função para pegar todos os clientes
def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

# Função para criar um novo cliente
def create_client(db: Session, name: str, email: str):
    db_client = models.Client(name=name, email=email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Função para pegar um cliente pelo ID
def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


# ========================================
# Funções de CRUD para Ativos (Assets)
# ========================================

# Função para listar todos os ativos
def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Asset).offset(skip).limit(limit).all()

# Função para criar um novo ativo
def create_asset(db: Session, ticker: str, name: str, price: float):
    db_asset = models.Asset(ticker=ticker, name=name, price=price)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

# Função para pegar um ativo pelo ID
def get_asset_by_id(db: Session, asset_id: int):
    return db.query(models.Asset).filter(models.Asset.id == asset_id).first()


# ========================================
# Funções de CRUD para Alocações (Allocations)
# ========================================

# Função para listar todas as alocações de um cliente
def get_allocations_by_client(db: Session, client_id: int):
    return db.query(models.Allocation).filter(models.Allocation.client_id == client_id).all()

# Função para criar uma nova alocação de ativo para o cliente
def create_allocation(db: Session, client_id: int, asset_id: int, quantity: float, price_at_purchase: float):
    db_allocation = models.Allocation(client_id=client_id, asset_id=asset_id, quantity=quantity, price_at_purchase=price_at_purchase)
    db.add(db_allocation)
    db.commit()
    db.refresh(db_allocation)
    return db_allocation

# Função para atualizar a quantidade de um ativo alocado a um cliente
def update_allocation(db: Session, allocation_id: int, quantity: float):
    db_allocation = db.query(models.Allocation).filter(models.Allocation.id == allocation_id).first()
    if db_allocation:
        db_allocation.quantity = quantity
        db.commit()
        db.refresh(db_allocation)
    return db_allocation

# Função para remover uma alocação
def delete_allocation(db: Session, allocation_id: int):
    db_allocation = db.query(models.Allocation).filter(models.Allocation.id == allocation_id).first()
    if db_allocation:
        db.delete(db_allocation)
        db.commit()
    return db_allocation
