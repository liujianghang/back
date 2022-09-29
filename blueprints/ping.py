from flask import Blueprint
from flask import jsonify


bp = Blueprint("ping", __name__, url_prefix="/ping")


@bp.route("/", methods=["GET", "POST"])
def ping():
    return jsonify('Pong!')
