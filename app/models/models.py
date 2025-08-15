from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Modelo de Cliente
class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    allocations = relationship("Allocation", back_populates="client")

# Modelo de Ativo Financeiro
class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    
    allocations = relationship("Allocation", back_populates="asset")

# Modelo de Alocação
class Allocation(Base):
    __tablename__ = 'allocations'
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)
    quantity = Column(Float, nullable=False)
    price_at_purchase = Column(Float, nullable=False)
    purchase_date = Column(DateTime, default=datetime.utcnow)
    
    client = relationship("Client", back_populates="allocations")
    asset = relationship("Asset", back_populates="allocations")

# Modelo de Rentabilidade Diária (para armazenar os preços diários)
class DailyReturn(Base):
    __tablename__ = 'daily_returns'
    
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    close_price = Column(Float, nullable=False)
    
    asset = relationship("Asset")
