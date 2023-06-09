from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from decimal import Decimal, getcontext, InvalidOperation

# Set the maximum precision to x digits
# This is important due to how floating point works in Python
# Try doing 1.1 + 2.1 in the console
getcontext().prec = 12

bp = Blueprint("calculator", __name__, url_prefix="/calculator")


@bp.route("/add", methods=("POST",))
def add():
    try:
        request_body = request.get_json()
        # Decimal has been used to avoid float rounding problems
        left_operand = Decimal(request_body.get("left_operand"))
        right_operand = Decimal(request_body.get("right_operand"))

        return {"result": left_operand + right_operand}
    except TypeError as error:
        abort(code=400, description="Missing some operands")
    except InvalidOperation as error:
        abort(code=400, description="Operands are not numbers")
    except Exception as error:
        abort(code=500, description="Unknown error")
