from seasons import translate_digits_to_text
from seasons import Person

def test_proper_data():
    assert translate_digits_to_text("0") == "zero"
    assert translate_digits_to_text("1234") == "one thousand, two hundred thirty-four"