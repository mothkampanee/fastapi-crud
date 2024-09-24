from pydantic import BaseModel

# 3: Pydantic Model
# 3.1: Base
class ItemBase(BaseModel):
    title: str
    description: str
    price: float

# 3.2: Request
class ItemCreated(ItemBase):
    pass

# 3.3: Response
class ItemResponse(ItemBase):
    id: int
    class Config:
        form_attributes = True