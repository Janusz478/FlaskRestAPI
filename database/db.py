from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Type: Product
def add(product):
    db.session.add(product)
    db.session.commit()

def reset():
    db.drop_all()
    db.create_all()

def add_category(category):
    db.session.add(category)
    db.session.commit()
    