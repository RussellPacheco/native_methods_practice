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
@pytest.mark.parametrize("test_input", [(3)])
def test_cap_three(test_input):
    with pytest.raises(TypeError):
        capitalize(test_input)

@pytest.mark.strings
@pytest.mark.center
@pytest.mark.parametrize("string,length,char,expected", [("hello", 10, " ", '  hello   '), ("love", 20, "-", '--------love--------')])
def test_center_one(string, length, char, expected):
    assert center(string, length, char) == expected

@pytest.mark.strings
@pytest.mark.center
@pytest.mark.parametrize("string,length,char,not_expected", [("hello", "hello"), ("russell", 16, "-", "----russell-----")])
def test_center_two(string, length, char, not_expected):
    assert center(string, length, char) != not_expected

@pytest.mark.strings
@pytest.mark.center
@pytest.mark.parametrize("string,length,char", [(3, 3, "-")])
def test_center_three(string, length, char):
    with pytest.raises(TypeError):
        center(string, length, char)

@pytest.mark.strings
@pytest.mark.count
@pytest.mark.parametrize("string,value,start,end,expected", ([("hello", "l", 0, -1, 2), ("the dog went to the park", "t", 12, -1, 2), ("hey you hey I like hey went hey", "hey", 0, 13, 2)]))
def test_count_one(string, value, start, end, expected):
    assert count(string, value, start, end) == expected

@pytest.mark.strings
@pytest.mark.count
@pytest.mark.parametrize("string,value,start,end,not_expected", (["hello", "l", 3, -1, 2]))
def test_count_two(string, value, start, end, not_expected):
    assert count(string, value, start, end) != not_expected
