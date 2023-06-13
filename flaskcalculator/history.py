from decimal import Decimal, InvalidOperation, getcontext

from flask import Blueprint, abort, flash, g, redirect, render_template, request, session, url_for

from flaskcalculator.db import get_db
from flaskcalculator.services.history.adapters import history_api
from flaskcalculator.services.history.service import HistoryService

MAXIMUM_HISTORY_SIZE = 3

bp = Blueprint("history", __name__, url_prefix="/calculator")


@bp.route("/history", methods=("GET",))
def add():
    try:
        return history_api.adapt(HistoryService().get_last_calculations())
    except Exception as error:
        abort(code=500, description="Unknown error")
