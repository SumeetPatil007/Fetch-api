from sqlalchemy.orm import Session
import models
import schemas


# CATEGORY CRUD

def get_categories(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def update_category(db: Session, category_id: int, category: schemas.CategoryCreate):
    db_category = get_category(db, category_id)

    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)

    return db_category


def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)

    if db_category:
        db.delete(db_category)
        db.commit()

    return db_category


# PRODUCT CRUD

def get_products(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)

    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.category_id = product.category_id

        db.commit()
        db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)

    if db_product:
        db.delete(db_product)
        db.commit()

    return db_product
