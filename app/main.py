from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from geopy.distance import geodesic
from typing import List

from app import models
from app import schemas
from app import crud
from app import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(database.get_db)):
    return crud.create_address(db=db, address=address)

@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(database.get_db)):
    db_address = crud.get_address(db=db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return crud.update_address(db=db, db_address=db_address, address_update=address)

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(database.get_db)):
    db_address = crud.get_address(db=db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    crud.delete_address(db=db, address_id=address_id)
    return {"detail": "Address deleted"}

@app.get("/addresses/", response_model=List[schemas.Address])
def get_addresses_within_distance(lat: float, lon: float, distance: float, db: Session = Depends(database.get_db)):
    addresses = crud.get_addresses(db=db)
    result = []
    for address in addresses:
        if geodesic((lat, lon), (address.latitude, address.longitude)).km <= distance:
            result.append(address)
    return result
