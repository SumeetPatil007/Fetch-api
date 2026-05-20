from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Machine Test")


# DATABASE CONNECTION

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# CATEGORY APIs

@app.get("/api/categories", response_model=list[schemas.CategoryResponse])
def get_categories(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit

    return crud.get_categories(db, skip=skip, limit=limit)


@app.post("/api/categories", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@app.get("/api/categories/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@app.put("/api/categories/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    updated_category = crud.update_category(db, category_id, category)

    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")

    return updated_category


@app.delete("/api/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)

    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted successfully"}


# PRODUCT APIs

@app.get("/api/products", response_model=list[schemas.ProductResponse])
def get_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit

    return crud.get_products(db, skip=skip, limit=limit)


@app.post("/api/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.get("/api/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@app.put("/api/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, product_id, product)

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)

    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}
