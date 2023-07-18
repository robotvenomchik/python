import home_lib2

def test_fixed_random():
    g=home_lib2.fixed_random() <=1000
    assert g <=1000 and g >=0