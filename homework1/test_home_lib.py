import home_lib
import pytest

def test_IsPasswordSuituble():
    assert home_lib.IsPasswordSuituble('Abcd1234!'), "normik"
    assert not home_lib.IsPasswordSuituble('short'), "<8"
    assert not home_lib.IsPasswordSuituble('onlylowercase'), "no low"
    assert not home_lib.IsPasswordSuituble('ONLYUPPERCASE'), "no up"
    assert not home_lib.IsPasswordSuituble('12345678'), "letters"
    assert not home_lib.IsPasswordSuituble('password without space'), "space pls"
    assert not home_lib.IsPasswordSuituble('no ascii символи'), "no asci"




