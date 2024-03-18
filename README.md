# DB and Web Project
# I Описание
Проект онлайн-магазина книг и канцелярских товаров.
## Наименование
Bookovka - онлайн книжный магазин 
## Предметная область
Учебный проект, онлайн-магазин товаров
# II Данные
## Для каждого элемента данных - ограничения
1. User Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор пользователя
     - email (String, Unique) - электронная почта пользователя
     - name (String) - имя пользователя
     - password (String) - пароль пользователя
     - is_superuser (Boolean, Default= false) - роль пользователя (true: Admin, false: User)
   - ForeignKey:
     - id_order (integer, Foreign Key referencing Order.id) - ссылка на идентификатор корзины пользователя

2. Basket Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор заказа
     - id_user (Integer) - идентификатор пользователя, сделавшего заказ
   - ForeignKey:
     - id_user (integer, Foreign Key referencing User.id) - ссылка на идентификатор пользователя заказа

3. BasketGoods Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор
     - id_basket (Integer) - идентификатор корзины
     - id_goods (Integer) - идентификатор товара
     - goods_amount (Integer, NotNull) - количество помещённого в корзину товара
   - ForeignKey:
     - id_basket (integer, Foreign Key referencing Basket.id) - ссылка на идентификатор корзины
     - id_goods (integer, Foreign Key referencing Goods.id) - ссылка на идентификатор товара

4. Goods Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор товара
     - name (String, NotNull) - название товара
     - description (String, Default="") - аннотация/описание товара
     - price (Integer, NotNull) - стоимость товара
     - amount (Integer, NotNull) - количество товара в магазине
     - id_brand (Integer) - "бренд" товара
     - id_subtype (Integer) - подтип товара
   - ForeignKey:
     - id_subtype (integer, Foreign Key referencing Subtype.id) - ссылка на идентификатор подтипа товара
     - id_brand (integer, Foreign Key referencing Brand.id) - ссылка на идентификатор бренда товара

5. Subtype Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор подтипа товара
     - name (String, Unique, NotNull) - название подтипа
     - id_type (Integer) - идентификатор типа подтипа
   - ForeignKey:
     - id_type (integer, Foreign Key referencing Type.id) - ссылка на идентификатор типа

6. Type Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор
     - name (String, Unique, NotNull) - название

7. Brand Table
   - Поля:
     - id (Integer, Primary Key, AutoIncrement) - идентификатор бренда
     - name (String, Unique, NotNull) - наименование бренда

## Общие ограничения целостности

## Схема базы данных
![image](https://github.com/AnatolyShev/DB-Web-project/assets/109897740/72be9ac9-a0e7-48dd-8c9a-8088dc174b97)

# III Пользовательские роли: наименование, ответственность, количество пользователей в этой роли

# IV UI/API
## UI
UI представляет собой набор страниц, с которыми взаимодейтсвует пользователь.
## API

# V Технологии разработки
## Фреймворки и библиотеки:
1. Backend: Node.js, FastApi, sqlalchemy, uvicorn
2. Frontend: React.js, Axios, react-router-dom 

## Языки программирования
1. Python
2. JavaScript

## СУБД
1. PostgreSQL
2. DBeaver 24.0.0

# VI Тестирование
