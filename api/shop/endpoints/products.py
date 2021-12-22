from flask import request
from api.myapi import api
from flask_restx import Resource
from api.shop.api_definition import page_with_products, product
from api.shop.domain_logic import create_product
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Product
from database import db as database

namespace = api.namespace("shop/products", description="Ops on my shop items")


# /api/shop/products
@namespace.route("/")
class Offer(Resource):
    @api.expect(pagination)
    @api.marshal_with(page_with_products)
    def get(self):
        database.add(Product("kuchen"))
        args = pagination.parse_args(request)
        page = args.get("page", 1)
        items_per_page = args.get("items_per_page", 10)
        products = Product.query.paginate(page, items_per_page, error_out=False)
        return products

    @api.expect(product)
    def post(self):
        create_product(request.json)
        return None, 200


@namespace.route("shop/<int:my_id>")
#@namespace.route("shop/<int:year>/<int:month>/")
@api.response(404, "There is not product with this ID yet")
class ProductItem(Resource):
    def get(self, my_id):
        return Product.query.filter(Product.id == my_id).one()
    # def put(self, id):

    # def delete(self, id):
