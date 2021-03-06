from flask_restx import fields
from api.myapi import api

product = api.model("Product", {
    "id": fields.Integer(readOnly=True, description="The identifier of the product"),
    "name": fields.String(required=True, description="Product name"),
    "category_id": fields.Integer(attribute="category.id"),
    "category_name": fields.String(attribute="category.name"),
})

product_add = api.model("Product for adding", {
    "name": fields.String(required=True, description="Product name"),
    "category_name": fields.String(attribute="category.name"),
})

category = api.model("Product category", {
    "id": fields.Integer(readOnly=True, description="The identifier of the category"),
    "name": fields.String(requiered=True, description="Category Name"),
})

page_with_products = api.inherit("Page with products", {
    "page": fields.Integer(description="Current page"),
    "pages": fields.Integer(description="Total pages"),
    "items_per_page": fields.Integer(description="Items per page"),
    "total_items": fields.Integer(description="Total amount of items"),
    "items": fields.List(fields.Nested(product)),
})
