from RestFolder.database.db import add
from RestFolder.database.dtos import Product

def create_product(data):
    name = data.get("name")
    product = Product(name)
    add(product)
    #TODO: add category

def read_product(data):
    pass


def update_product(data):
    pass


def delete_product(data):
    pass

#TODO: implement read, update, delete