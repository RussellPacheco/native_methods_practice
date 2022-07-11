import pytest
from src import *

@pytest.mark.strings
@pytest.mark.capitalize
@pytest.mark.parametrize("test_input,expected", [("hello", "Hello"), ("russell", "Russell"), ("Jocelyn", "Jocelyn")])
def test_cap_one(test_input, expected):
    assert capitalize(test_input) == expected


@pytest.mark.strings
@pytest.mark.capitalize
@pytest.mark.parametrize("test_input, expected", [("hello", "hello"), ("Russell", "russell"), ("jocelyn", "JOCELYN")])
def test_cap_two(test_input, expected):
    assert capitalize(test_input) != expected

@pytest.mark.strings
@pytest.mark.capitalize
@pytest.mark.parametrize("test_input, expected", [(3, TypeError)])
def test_cap_three(test_input, expected):
    with pytest.raises(TypeError):
        capitalize(test_input)

@pytest.mark.strings
@pytest.mark.center
@pytest.mark.parametrize("string, length, char, expected", [("hello", 10, " ", '  hello   '), ("love", 20, "-", '--------love--------')])
def test_center_one(string, length, char, expected):
    assert center(string, length, char) == expected

@pytest.mark.strings
@pytest.mark.center
@pytest.mark.parametrize("string, length, ")