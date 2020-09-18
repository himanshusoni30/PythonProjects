from psutils import power

def test_power_1():
    assert power(2,3)==8

def test_power_2():
    assert power(2,3) != 18