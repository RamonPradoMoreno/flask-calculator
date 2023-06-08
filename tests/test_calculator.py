import pytest
from flask import g, session
from flaskr.db import get_db


def test_add(client, app):
    assert (
        client.post(
            path="/calculator/add",
            json={"left_operand": 1, "right_operand": 2},
        ).status_code
        == 200
    )
