from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from decimal import Decimal, getcontext, InvalidOperation
from flaskcalculator.db import get_db
from flaskcalculator.services.calculator.calculation import SupportedCalculation
from flaskcalculator.services.calculator.adapters import api_calculator
from flaskcalculator.services.calculator.errors import MissingOperandError, OperandError

# Set the maximum precision to x digits
# This is important due to how floating point works in Python
# Try doing 1.1 + 2.1 in the console
getcontext().prec = 12

bp = Blueprint("calculator", __name__, url_prefix="/calculator")


@bp.route("/add", methods=("POST",))
def add():
    operation = SupportedCalculation.ADDITION.value
    try:
        db = get_db()
        request_body = request.get_json()

        left_operand = request_body.get("left_operand")
        right_operand = request_body.get("right_operand")
        result = api_calculator.adapt(left_operand=left_operand, right_operand=right_operand, operation=operation)
        return {"result": result}
    except MissingOperandError as error:
        abort(code=400, description=error.message)
    except OperandError as error:
        abort(code=400, description=error.message)
    except Exception as error:
        abort(code=500, description="Unknown error")
