import pytest
from assertpy import assert_that
from app import insert_user, get_users, update_user, delete_user, create_table


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    create_table()


def test_insert_user():
    insert_user("Max Asofiev", 30)
    users = get_users()
    assert_that(users).extracting(0, 1).contains(("Max Asofiev", 30))


def test_update_user():
    insert_user("Lilia Bulka", 25)
    users = get_users()
    user_id = users[-1][0]
    update_user(user_id, "Lilia Pitter", 26)
    users = get_users()
    assert_that(users).extracting(0, 1).contains(("Lilia Pitter", 26))


def test_delete_user():
    insert_user("Mark Brown", 35)
    users = get_users()
    user_id = users[-1][0]
    delete_user(user_id)
    users = get_users()
    assert_that(users).extracting(0).does_not_contain(user_id)
