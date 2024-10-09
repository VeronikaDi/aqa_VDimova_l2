import pytest
import logging
from logger import setup_logger
from assertpy import assert_that

setup_logger()


@pytest.mark.usefixtures("authenticated_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 7),
        ("engine_volume", 10),
        ("brand", 3),
        ("price", None),
        ("year", 20),
        ("engine_volume", 15)
    ])
    def test_search_cars(self, authenticated_session, sort_by, limit):

        logging.info(f"Starting test_search_cars with sort_by={sort_by} and limit={limit}")

        params = {"sort_by": sort_by}
        if limit is not None:
            params["limit"] = limit

        url = 'http://127.0.0.1:8080/cars'
        response = authenticated_session.get(url, params=params)

        logging.info(f"Request params: {params}")
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response data: {response.json()}")

        assert_that(response.status_code).is_equal_to(200)

        cars_data = response.json()
        assert_that(cars_data).is_instance_of(list)

        if limit is not None:
            assert_that(len(cars_data)).is_less_than_or_equal_to(limit)

        required_keys = {"brand", "year", "engine_volume", "price"}
        for car in cars_data:
            assert_that(car.keys()).contains(*required_keys)
