from flask import request
from api.myapi import api, user_auth
from flask_restx import Resource
from api.shop.api_definition import page_with_products, product
from api.shop.domain_logic import create_product
from api.shop.parsers import pagination_parser as pagination
from database.dtos import Product
from database import db as database
import hashlib

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
    @api.doc(security="basicAuth")
    @api.response(200, "Success")
    @api.response(403, "Forbidden")
    def post(self):
        req_auth = request.authorization
        if req_auth and req_auth.username == user_auth["username"] and \
                hashlib.sha256(req_auth.password.encode()).hexdigest() == user_auth["hashed_password"]:
            create_product(request.json)
            return None, 200
        else:
            return None, 403


@namespace.route("shop/<int:my_id>")
#@namespace.route("shop/<int:year>/<int:month>/")
@api.response(404, "There is not product with this ID yet")
class ProductItem(Resource):
    def get(self, my_id):
        return Product.query.filter(Product.id == my_id).one()
    # def put(self, id):

    # def delete(self, id):
