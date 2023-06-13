from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from decimal import Decimal, getcontext, InvalidOperation
from flaskcalculator.db import get_db

# Set the maximum precision to x digits
# This is important due to how floating point works in Python
# Try doing 1.1 + 2.1 in the console
getcontext().prec = 12

bp = Blueprint("calculator", __name__, url_prefix="/calculator")


@bp.route("/add", methods=("POST",))
def add():
    try:
        db = get_db()
        request_body = request.get_json()
        # Decimal has been used to avoid float rounding problems
        left_operand = Decimal(request_body.get("left_operand"))
        right_operand = Decimal(request_body.get("right_operand"))
        result = left_operand + right_operand
        # Decimals have to be converted to string so SQLite understands them
        db.execute(
            "INSERT INTO history (operation, left_operand, right_operand, result)" " VALUES (?, ?, ?, ?)",
            ("addition", str(left_operand), str(right_operand), str(result)),
        )
        db.commit()
        return {"result": float(result)}
    except TypeError as error:
        abort(code=400, description="Missing some operands")
    except InvalidOperation as error:
        abort(code=400, description="Operands are not numbers")
    except Exception as error:
        abort(code=500, description="Unknown error")
