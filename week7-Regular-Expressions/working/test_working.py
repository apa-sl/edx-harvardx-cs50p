import pytest
from working import convert

def test_max_range():
    """Check that convert handles maximum time ranges."""
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_mixed_formats():
    """Check that convert raises ValueErrors mixing 12H and 24H time."""
    with pytest.raises(ValueError):
        convert("08:00 to 16:00")


def test_out_of_range_hours():
    """Check that convert raises ValueErrors when hour ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("13:00 AM to 20:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 20 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")


def test_out_of_range_minutes():
    """Check that convert raises ValueErrors when minute ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("12:99 AM to 5:69 PM")


def test_no_entry():
    """Check that convert raises ValueErrors when there is no input."""
    with pytest.raises(ValueError):
        convert("")


def test_invalid_format():
    """Check that convert raises ValueErrors when time is inproperly formated"""
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")