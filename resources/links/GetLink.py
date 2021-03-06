from flask_restful import Resource
from flasgger import swag_from
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from common.DbHandler import DbHandler


class GetLink(Resource):
    @jwt_required
    @swag_from('../../yml/links_get.yml')
    def get(self, id=-1):
        """ If client requests for /links will get whole links;
        else if requests for /links/[ID] will get specified link.
        NOTE: -1 is used as sentinel value
        """
        current_user_username = get_jwt_identity()
        links_list = DbHandler.get_links(current_user_username, id)
        if links_list:
            return make_response(
                jsonify(links_list),
                200
            )
        else:
            return make_response(
                jsonify(msg="Link not found!"),
                404
            )
