import pytest
from flask import g, session
from flaskcalculator.db import get_db
from decimal import Decimal


def test_returns_200(client, app):
    response = client.post(
        path="/calculator/add",
        json={"left_operand": 1, "right_operand": 2},
    )
    assert response.status_code == 200


@pytest.mark.parametrize(
    ("left_operand", "right_operand", "message"),
    (
        (None, None, b"At least one operand is missing"),
        (1, None, b"At least one operand is missing"),
        (None, 1, b"At least one operand is missing"),
    ),
)
def test_add_validate_input_not_empty(client, left_operand, right_operand, message):
    response = client.post(
        path="/calculator/add",
        json={
            "left_operand": left_operand,
            "right_operand": right_operand,
        },
    )
    assert message in response.data


@pytest.mark.parametrize(
    ("left_operand", "right_operand", "message"),
    (
        ("hello", "1", b"At least one operand is not a number"),
        ("1", "hello", b"At least one operand is not a number"),
        ("1,1", "1,1", b"At least one operand is not a number"),
    ),
)
def test_add_validate_input_number(client, left_operand, right_operand, message):
    response = client.post(
        path="/calculator/add",
        json={
            "left_operand": left_operand,
            "right_operand": right_operand,
        },
    )
    assert message in response.data


@pytest.mark.parametrize(
    ("left_operand", "right_operand", "result"),
    (
        (1, 1, 2),
        (1.1, 2.2, 3.3),
        (1, -1, 0),
        (-1, 1, 0),
        (-1, -1, -2),
    ),
)
def test_add_works(client, left_operand, right_operand, result):
    response = client.post(
        path="/calculator/add",
        json={
            "left_operand": left_operand,
            "right_operand": right_operand,
        },
    )
    assert Decimal(response.json.get("result")) == Decimal(result)


def test_storing_in_db_max_precision(app, client):
    # Cannot use 1e-11 because the sql script already inserted that row
    response = client.post(
        path="/calculator/add",
        json={
            "left_operand": 3e-11,
            "right_operand": 4e-11,
        },
    )
    assert Decimal(response.json.get("result")) == Decimal(7e-11)
    with app.app_context():
        db = get_db()
        history = db.execute("SELECT * FROM history WHERE result=7e-11").fetchone()
        assert history is not None
