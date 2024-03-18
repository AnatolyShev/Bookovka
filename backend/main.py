from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
import pydantic
from starlette import status
import schemas as sh
from database import engine, get_db, db_dependency
import models as md
import auth
from auth import bcrypt_context, get_current_user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router)
md.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Замените * на список разрешенных источников, если это возможно
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Добавьте здесь необходимые методы
    allow_headers=["*"],  # Разрешаем все заголовки, это может быть настроено более строго
)

user_dependency = Annotated[dict, Depends(get_current_user)]
#uvicorn main:app --reload

@app.get("/api/")
async def root():
    return {"message": "DB-Web project"}

@app.post("/api/user")
async def create_user(user: sh.UserBase, db: db_dependency):
    db_user = md.User(email=user.email, name=user.name, password= bcrypt_context.hash(user.password), is_superuser=user.is_superuser)
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    new_user = db.query(md.User).filter(md.User.email == user.email).first()
    db_basket = md.Basket(user_id=new_user.id)
    db.add(db_basket)
    db.commit()    
    db.refresh(db_basket)

@app.get("/api/user")
async def get_all_users(db: db_dependency):
    users = db.query(md.User)
    result = []
    for user in users:
        result.append({"user_id": user.id, "email": user.email, "username": user.name, "is_superuser": user.is_superuser})
        #добавлять ли расшифровку паролей?
    return result

@app.post("/api/goods")
async def create_goods(goods: sh.GoodsBase, db: db_dependency):
    db_goods = md.Good(name=goods.name, price= goods.price, amount=goods.amount, description=goods.description, brand_id=goods.brand_id, subtype_id=goods.subtype_id)
    db.add(db_goods)
    db.commit()
    db.refresh(db_goods)

@app.get("/api/goods")
async def get_all_goods(db: db_dependency):
    goodss = db.query(md.Good)
    result = []
    for goods in goodss:
        result.append({"goods_id": goods.id, "goods": goods.name, "price": goods.price, "amount": goods.amount, "description": goods.description, "brand_id": goods.brand_id, "subtype_id": goods.subtype_id})
    return result

@app.post("/api/basket")
async def create_basket(basket: sh.BasketBase, db: db_dependency):
    db_basket = md.Basket(user_id=basket.user_id)
    db.add(db_basket)
    db.commit()
    db.refresh(db_basket)

@app.get("/api/basket")
async def get_all_baskets(db: db_dependency):
    baskets = db.query(md.Basket)
    result = []
    for basket in baskets:
        result.append({"basket_id": basket.id, "basket_user_id": basket.user_id})
    return result

@app.post("/api/brand")
async def create_brand(brand: sh.BrandBase, db: db_dependency):
    db_brand = md.Brand(name=brand.name)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)

@app.get("/api/brand")
async def get_all_brands(db: db_dependency):
    brands = db.query(md.Brand)
    result = []
    for brand in brands:
        result.append({"brand_id": brand.id, "brand": brand.name})
    return result

@app.post("/api/type")
async def create_type(type: sh.TypeBase, db: db_dependency):
    db_type = md.Type(name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)

@app.get("/api/type")
async def get_all_types(db: db_dependency):
    types = db.query(md.Type)
    result = []
    for type in types:
        result.append({"type_id": type.id, "type": type.name})
    return result

@app.post("/api/subtype")
async def create_subtype(subtype: sh.SubTypeBase, db: db_dependency):
    db_subtype = md.SubType(name=subtype.name, type_id=subtype.type_id)
    db.add(db_subtype)
    db.commit()
    db.refresh(db_subtype)

@app.get("/api/subtype")
async def get_all_subtypes(db: db_dependency):
    subtypes = db.query(md.SubType)
    result = []
    for subtype in subtypes:
        result.append({"subtype_id": subtype.id, "subtype": subtype.name, "type_id": subtype.type_id})
    return result

@app.post("/api/basket_goods")
async def create_basket_goods(basket_goods: sh.BasketGoodsBase, db: db_dependency):
    db_basket_goods = md.BasketGoods(goods_id=basket_goods.goods_id, basket_id=basket_goods.basket_id, goods_amount=basket_goods.goods_amount)
    db.add(db_basket_goods)
    db.commit()
    db.refresh(db_basket_goods)

@app.get("/api/basket_goods")
async def get_all_basket_goods(db: db_dependency):
    basket_goodss = db.query(md.BasketGoods)
    result = []
    for basket_goods in basket_goodss:
        result.append({"basket_goods_id": basket_goods.id, "goods_id": basket_goods.goods_id, "basket_id": basket_goods.basket_id, "goods_amount": basket_goods.goods_amount})
    return result

@app.get("/api/user/{user_id}")
async def get_user(user_id: int, db: db_dependency):
    result = db.query(md.User).filter(md.User.id == user_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="User with this id isn't found")
    return result

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authintification failed")
    return {"User": user}

@app.delete("/api/user/{user_id}")
async def delete_user_by_id(user_id: int, db: db_dependency):
    user = db.query(md.User).filter(md.User.id == user_id).first()
    user_basket = db.query(md.Basket).filter(md.Basket.user_id == user_id).first()
    user_basket_goodss = db.query(md.BasketGoods).filter(md.BasketGoods.basket_id == user_basket.id)
    for user_basket_goods in user_basket_goodss:
        db.delete(user_basket_goods)
    db.delete(user_basket)
    db.delete(user)
    db.commit()
    return {"User": user}

@app.delete("/api/goods/{id}")
async def delete_goods_by_id(goods_id: int, db: db_dependency):
    goods = db.query(md.Good).filter(md.Good.id == goods_id).first()
    user_basket_goodss = db.query(md.BasketGoods).filter(md.BasketGoods.goods_id == goods_id)
    for user_basket_goods in user_basket_goodss:
        db.delete(user_basket_goods)
    db.delete(goods)
    db.commit()
    return {"Goods": goods}

@app.delete("/api/subtype/{id}")
async def delete_single_subtype_by_id(subtype_id: int, db: db_dependency):
    subtype = db.query(md.SubType).filter(md.SubType.id == subtype_id).first()
    goodss = db.query(md.Good).filter(md.Good.subtype_id == subtype_id)
    for goods in goodss:
        goods.subtype_id = None
    db.delete(subtype)
    db.commit()
    return {"Type": subtype}

@app.delete("/api/subtype_cascade/{id}")
async def delete_subtype_by_id_cascade(subtype_id: int, db: db_dependency):
    subtype = db.query(md.SubType).filter(md.SubType.id == subtype_id).first()
    goodss = db.query(md.Good).filter(md.Good.subtype_id == subtype_id)

    for goods in goodss:
        basket_goodss = db.query(md.BasketGoods).filter(md.BasketGoods.goods_id == goods.id)
        for basket_goods in basket_goodss:
            db.delete(basket_goods)
        db.delete(goods)
    db.delete(subtype)
    db.commit()
    return {"Subype": subtype}

@app.delete("/api/type/{id}")
async def delete_single_type_by_id(type_id: int, db: db_dependency):
    type = db.query(md.Type).filter(md.Type.id == type_id).first()
    subtypes = db.query(md.SubType).filter(md.SubType.type_id == type_id)
    for subtype in subtypes:
        subtype.type_id = None
    db.delete(type)
    db.commit()
    return {"Type": type}

@app.delete("/api/brand/{id}")
async def delete_single_brand_by_id(brand_id: int, db: db_dependency):
    brand = db.query(md.Brand).filter(md.Brand.id == brand_id).first()
    goodss = db.query(md.Good).filter(md.Good.brand_id == brand_id)
    for goods in goodss:
        goods.brand_id = None
    db.delete(brand)
    db.commit()
    return {"Brand": brand}

@app.delete("/api/basket_goods/{id}")
async def delete_single_basket_goods_by_id(basket_goods_id: int, db: db_dependency):
    basket_goods = db.query(md.BasketGoods).filter(md.BasketGoods.id == basket_goods_id).first()
    db.delete(basket_goods)
    db.commit()
    return {"BasketGoods": basket_goods}

@app.get("/api/goods/{id}")
async def get_goods_by_id(goods_id: int, db: db_dependency):
    result = db.query(md.Good).filter(md.Good.id == goods_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Goods with this id isn't found")
    return result

@app.get("/api/brand/{id}")
async def get_brand_by_id(brand_id: int, db: db_dependency):
    result = db.query(md.Brand).filter(md.Brand.id == brand_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Brand with this id isn't found")
    return result

@app.get("/api/type/{id}")
async def get_type_by_id(type_id: int, db: db_dependency):
    result = db.query(md.Type).filter(md.Type.id == type_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Type with this id isn't found")
    return result

@app.get("/api/subtype/{id}")
async def get_subtype_by_id(subtype_id: int, db: db_dependency):
    result = db.query(md.SubType).filter(md.SubType.id == subtype_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Subtype with this id isn't found")
    return result

@app.get("/api/basket/{id}")
async def get_basket_by_id(basket_id: int, db: db_dependency):
    result = db.query(md.Basket).filter(md.Basket.id == basket_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Basket with this id isn't found")
    return result

@app.get("/api/basket_goods/{id}")
async def get_basket_goods_by_id(basket_goods_id: int, db: db_dependency):
    result = db.query(md.BasketGoods).filter(md.BasketGoods.id == basket_goods_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Basket_goods with this id isn't found")
    return result

@app.get("/api/goods/condition")
async def get_goods_by_condition(db: db_dependency, id: int | None= None, 
                                 name: str | None= None, 
                                 price1: int | None = None, 
                                 price2: int | None = None, 
                                 amount1: int | None = None, 
                                 amount2: int | None = None, 
                                 oper1: str | None=None,
                                 oper2: str | None=None,
                                 oper3: str | None=None,
                                 oper4: str | None=None,
                                 oper5: str | None=None,
                                 oper6: str | None=None,
                                 value1: int | None=None,
                                 value2: str | None=None,
                                 value3: int | None=None,
                                 value4: int | None=None,
                                 value5: int | None=None,
                                 value6: int | None=None):

    return 0