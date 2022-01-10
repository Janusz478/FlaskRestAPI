from database.db import db, Product, Category, add_product, add_category, add_if_not_exists_category

def create_product(data):
    name = data.get("name")
    category_name = data.get("category_name")
    if category_name:
        category_id = add_if_not_exists_category(category_name)
        product = Product(name=name, category_id=category_id)
    else:
        product = Product(name=name)
    add_product(product)
    return product, 200

def read_product(data):
    pass


def update_product(identifier, data):
    product = Product.query.filter_by(id=identifier).first()
    if product is None:
        return None, 404
    name = data.get("name")
    category_name = data.get("category_name")
    if category_name:
        category_id = add_if_not_exists_category(category_name)
        product.category_id = category_id
    product.name = name
    db.session.commit()
    return None, 200


def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()

#TODO: implement read, update, delete