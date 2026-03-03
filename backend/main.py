from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from typing import List, Optional

# Database setup
DATABASE_URL = "sqlite:///./items.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB Model (this becomes your database table)
class ItemDB(Base):
    __tablename__ = "items"
    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at  = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)  # creates items.db file automatically

# Pydantic schemas (for request/response validation)
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

# Create the FastAPI app
app = FastAPI(title="Items API", version="1.0.0")

# Allow frontend to talk to backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ENDPOINTS
@app.get("/")
def root():
    return {"status": "running", "message": "Items API is live"}

@app.get("/items", response_model=List[ItemResponse])
def get_items(db=Depends(get_db)):
    return db.query(ItemDB).order_by(ItemDB.id.desc()).all()

@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db=Depends(get_db)):
    if not item.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    db_item = ItemDB(name=item.name.strip(), description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db=Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted"}