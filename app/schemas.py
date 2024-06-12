from pydantic import BaseModel

class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    street: str = None
    city: str = None
    state: str = None
    country: str = None
    latitude: float = None
    longitude: float = None

class Address(AddressBase):
    id: int

    class Config:
        from_attributes = True
