import pytest

import crypto_lib

@pytest.mark.parametrize('value, expected', [('qwerty','66fe6c41a665b25ca038d7044b595065')])
def test_encode_md5(value, expected):
    assert crypto_lib.encode_md5(value) == expected

def test_passlib_data():
    hashes=set()
    for _ in range (1000):
        hashes.add(crypto_lib.get_password_hash('1'))
    assert len(hashes)==1000