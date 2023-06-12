from decimal import Decimal, InvalidOperation, getcontext

from flask import Blueprint, abort, flash, g, redirect, render_template, request, session, url_for

from flaskr.db import get_db

MAXIMUM_HISTORY_SIZE = 3

bp = Blueprint("history", __name__, url_prefix="/calculator")


@bp.route("/history", methods=("GET",))
def add():
    result = []
    try:
        db = get_db()
        history = db.execute(
            "SELECT created, operation, left_operand, right_operand, result " " FROM history" " ORDER BY created DESC"
        ).fetchmany(MAXIMUM_HISTORY_SIZE)
        for row in history:
            row_dict = dict(row)
            row_dict["created"] = row_dict["created"].isoformat()
            result.append(row_dict)

        return result
    except Exception as error:
        abort(code=500, description="Unknown error")
