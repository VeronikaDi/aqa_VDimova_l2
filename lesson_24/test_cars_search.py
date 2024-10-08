import pytest
from logger import setup_logger
import logging

setup_logger()


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 7),
    ("engine_volume", 10),
    ("brand", 3),
    ("price", None),
    ("year", 20),
    ("engine_volume", 15)
])
def test_search_cars(authenticated_session, sort_by, limit):

    logging.info("Starting test_search_cars with sort_by=%s and limit=%s", sort_by, limit)

    params = {"sort_by": sort_by}
    if limit is not None:
        params["limit"] = limit

    url = 'http://127.0.0.1:8080/cars'
    response = authenticated_session.get(url, params=params)

    logging.info(f"Request params: {params}")
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response.json()}")

    assert response.status_code == 200, "Failed to retrieve cars data"

    cars_data = response.json()
    assert isinstance(cars_data, list), "Cars data is not a list"

    if limit is not None:
        assert len(cars_data) <= limit, "Number of cars exceeds limit"

    required_keys = {"brand", "year", "engine_volume", "price"}
    for car in cars_data:
        assert required_keys.issubset(car.keys()), f"Missing keys in car data: {car}"
