import pydantic as pd
from tkinter.messagebox import NO

class UserBase(pd.BaseModel):
    email: str
    name: str
    password: str
    is_superuser: bool

class BasketBase(pd.BaseModel):
    user_id: int

class GoodsBase(pd.BaseModel):
    name: str
    price: int
    amount: int
    description: str
    brand_id: int
    subtype_id: int

class BrandBase(pd.BaseModel):
    name: str

class SubTypeBase(pd.BaseModel):
    name: str
    type_id: int

class TypeBase(pd.BaseModel):
    name: str

class BasketGoodsBase(pd.BaseModel):
    goods_id: int
    basket_id: int
    goods_amount: int

class Token(pd.BaseModel):
    access_token: str
    token_type:str