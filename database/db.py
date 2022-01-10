from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    products = db.relationship("Product", backref="category")

#Type: Product
def add_product(product):
    db.session.add(product)
    db.session.commit()

def reset():
    db.drop_all()
    db.create_all()

def add_category(category):
    db.session.add(category)
    db.session.commit()

def add_if_not_exists_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    if category is not None:
        category_id = category.id
    else:
        db.session.add(Category(name=category_name))
        db.session.commit()
        category = Category.query.filter_by(name=category_name).first()
        category_id = category.id
    return category_id

