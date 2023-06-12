def test_returns_200(client, app):
    response = client.get(
        path="/calculator/history",
    )
    assert response.status_code == 200


def test_validate_output(client, app):
    response = client.get(
        path="/calculator/history",
    )
    assert response.json == [
        {
            "created": "2023-01-04T00:00:00",
            "operation": "addition",
            "left_operand": 1e-11,
            "right_operand": 1e-11,
            "result": 2e-11,
        },
        {
            "created": "2023-01-03T00:00:00",
            "operation": "addition",
            "left_operand": 1.0,
            "right_operand": -1.0,
            "result": 0.0,
        },
        {
            "created": "2023-01-02T00:00:00",
            "operation": "addition",
            "left_operand": -1.0,
            "right_operand": -1.0,
            "result": -2.0,
        },
    ]
