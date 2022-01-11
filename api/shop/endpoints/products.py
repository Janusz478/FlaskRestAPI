from flask import request
from api.myapi import api, authorize
from flask_restx import Resource
from api.shop.api_definition import page_with_products, product, product_add
from api.shop.domain_logic import create_product, update_product, delete_product
from api.shop.parsers import pagination_parser
from database.db import Product

namespace = api.namespace("shop/products", description="Ops on my shop items")


# /api/shop/products
@namespace.route("/")
class Offer(Resource):
    @api.expect(pagination_parser)
    @api.marshal_with(page_with_products)
    def get(self):
        args = pagination_parser.parse_args(request)
        page = args.get("page", 1)
        items_per_page = args.get("items_per_page", 10)
        product_name = args.get("product_name")
        if product_name:
            products = Product.query.filter(Product.name.like("%{}%".format(product_name))).paginate(page,
                                                                                                     items_per_page,
                                                                                                     error_out=False)
        else:
            products = Product.query.paginate(page, items_per_page, error_out=False)
        return products

    @api.expect(product_add)
    @api.doc(security="basicAuth")
    @api.response(200, "Success")
    @api.response(403, "Forbidden")
    @api.response(400, "Bad Request, Product was wrong")
    @api.marshal_with(product)
    def post(self):
        if authorize(request):
            return create_product(request.json)
        else:
            return None, 403


@namespace.route("/<int:id>")
@api.response(200, "Success")
@api.response(404, "There is not product with this ID yet")
class ProductItem(Resource):
    @api.marshal_with(product)
    def get(self, id):
        return Product.query.filter(Product.id == id).one()

    @api.response(403, "Forbidden")
    @api.expect(product_add)
    @api.doc(security="basicAuth")
    def put(self, id):
        if authorize(request):
            return update_product(id, request.json)
        else:
            return None, 403

    @api.response(403, "Forbidden")
    @api.doc(security="basicAuth")
    def delete(self, id):
        if authorize(request):
            return delete_product(id)
        else:
            return None, 403
