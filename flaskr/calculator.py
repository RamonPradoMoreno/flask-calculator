from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort

bp = Blueprint("calculator", __name__, url_prefix="/calculator")


@bp.route("/add", methods=("POST",))
def add():
    try:
        request_body = request.get_json()
        left_operand = request_body.get("left_operand")
        right_operand = request_body.get("right_operand")
        return {"result": left_operand + right_operand}
    except Exception as error:
        abort(code=400, description="Missing some operands")
