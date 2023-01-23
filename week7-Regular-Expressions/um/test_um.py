from um import count

def test_no_um():
    assert count("Whatever") == 0
    assert count("Gum is yummy") == 0

def test_um():
    assert count("UM") == 1r
    assert count("Regular, um, expressions") == 1
    assert count("Um, I really um... I um want to, um?") == 4