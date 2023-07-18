import home_lib
import pytest


def test_is_password_suituble():
    assert home_lib.is_password_suituble('Abcd1234!'), "normik"
    assert not home_lib.is_password_suituble('short'), "<8"
    assert not home_lib.is_password_suituble('onlylowercase'), "no low"
    assert not home_lib.is_password_suituble('ONLYUPPERCASE'), "no up"
    assert not home_lib.is_password_suituble('12345678'), "letters"
    assert not home_lib.is_password_suituble('password without space'), "space pls"
    assert not home_lib.is_password_suituble('no ascii символи'), "no asci"
