import sqlalchemy as _sql
from database import Base

class User(Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True)
    name = _sql.Column(_sql.String)
    password = _sql.Column(_sql.String)
    is_superuser = _sql.Column(_sql.Boolean, default=False)

class Basket(Base):
    __tablename__ = "baskets"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))

class Good(Base):
    __tablename__ = "goods"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False)
    price = _sql.Column(_sql.Integer, nullable=False)
    amount = _sql.Column(_sql.Integer, nullable=False)
    description = _sql.Column(_sql.String, default="")
    brand_id = _sql.Column(_sql.Integer, _sql.ForeignKey("brands.id"))
    subtype_id = _sql.Column(_sql.Integer, _sql.ForeignKey("subtypes.id"))

class Brand(Base):
    __tablename__ = "brands"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, nullable=False)

class Type(Base):
    __tablename__ = "types"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, nullable=False)


class SubType(Base):
    __tablename__ = "subtypes"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, nullable=False)
    type_id = _sql.Column(_sql.Integer, _sql.ForeignKey("types.id"))

class BasketGoods(Base):
    __tablename__ = "basket_goods"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    goods_id = _sql.Column(_sql.Integer, _sql.ForeignKey("goods.id"))
    basket_id = _sql.Column(_sql.Integer, _sql.ForeignKey("baskets.id"))
    goods_amount = _sql.Column(_sql.Integer, nullable=False)