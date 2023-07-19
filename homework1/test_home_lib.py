import home_lib
import pytest

test_cases=[
    ("Abcd1234!",True),
    ("Ab2!",False),
    ("sadsad!12",False),
    ("FBSFS!23",False),
    ("2145!",False),
    ("пепа!",False),
]
@pytest.mark.parametrize('password, expected', test_cases)
def test_is_password_suituble(password,expected):
    assert home_lib.is_password_suituble(password)==expected

