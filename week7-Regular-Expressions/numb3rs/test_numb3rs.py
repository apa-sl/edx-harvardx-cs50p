from numb3rs import validate

def test_proper_IPv4():
    assert validate("0.123.245.255") == True
    assert validate("123.243.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_IPv4():
    assert validate("0.0.0") == False
    assert validate("255.999.123.123") == False
    assert validate("256.256.400.300") == False
    assert validate("cat") == False
    assert validate("9999.9999.1233.2341")  == False
    assert validate("192.192.192.192.192") == False