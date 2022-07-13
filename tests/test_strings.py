import pytest
from src.strings import *

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
@pytest.mark.parametrize("string,length,char,not_expected", [("hello", 10, " " , "hello"), ("russell", 16, "-", "----russell-----")])
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
@pytest.mark.parametrize("string,value,start,end,expected", [("hello", "l", 0, -1, 2), ("the dog went to the park", "t", 12, -1, 2), ("hey you hey I like hey went hey", "hey", 0, 13, 2)])
def test_count_one(string, value, start, end, expected):
    assert count(string, value, start, end) == expected

@pytest.mark.strings
@pytest.mark.count
@pytest.mark.parametrize("string,value,start,end,not_expected", [("hello", "l", 3, -1, 2)])
def test_count_two(string, value, start, end, not_expected):
    assert count(string, value, start, end) != not_expected

@pytest.mark.strings
@pytest.mark.count
@pytest.mark.parametrize("string,value", [(42, 2)])
def test_count_three(string, value):
    with pytest.raises(TypeError):
        count(string, value)

@pytest.mark.strings
@pytest.mark.index
@pytest.mark.parametrize("string,value,start,end,expected", [("hello", "l", 0, -1, 2), ("russell", "s", 3, -1, 3), ("the dog went to the park", "park", 0, -1, 20)])
def test_index_one(string, value, start, end, expected):
    assert index(string, value, start, end) == expected

@pytest.mark.strings
@pytest.mark.index
@pytest.mark.parametrize("string,value,start,end,not_expected", [("hello", "l", 3, -1, 2), ("russell", "l", 0, -1, 6)])
def test_index_two(string, value, start, end, not_expected):
    assert index(string, value, start, end) != not_expected

@pytest.mark.strings
@pytest.mark.index
@pytest.mark.parametrize("string,value", [(3423, 3)])
def test_index_three(string, value):
    with pytest.raises(TypeError):
        index(string, value)

@pytest.mark.strings
@pytest.mark.islower
@pytest.mark.parametrize("string,expected", [("hello", True), ("RUSSELL", False), ("jocelyN", False)])
def test_islower_one(string, expected):
    assert islower(string) == expected

@pytest.mark.strings
@pytest.mark.islower
@pytest.mark.parametrize("string,not_expected", [("hello", False), ("russeLL", True), ("JOCELYN", True)])
def test_islower_two(string, not_expected):
    assert islower(string) != not_expected

@pytest.mark.strings
@pytest.mark.islower
@pytest.mark.parametrize("string", [(2343)])
def test_islower_three(string):
    with pytest.raises(TypeError):
        islower(string)

@pytest.mark.strings
@pytest.mark.isnumeric
@pytest.mark.parametrize("string,expected", [("243234", True), ("3432fk3232", False), ("kjdkjfkd", False)])
def test_isnumeric_one(string, expected):
    assert isnumeric(string) == expected

@pytest.mark.strings
@pytest.mark.isnumeric
@pytest.mark.parametrize("string,not_expected", [("dfjdskjf", True), ("32432", False)])
def test_isnumeric_two(string, not_expected):
    assert isnumeric(string) != not_expected

@pytest.mark.strings
@pytest.mark.isnumeric
@pytest.mark.parametrize("string", [(34234)])
def test_isnumeric_three(string):
    with pytest.raises(TypeError):
        isnumeric(string)

@pytest.mark.strings
@pytest.mark.join
@pytest.mark.parametrize("iterable,separator,expected", [([1,2,3], "+", "1+2+3"), ("abc", "+", "a+b+c")])
def test_join_one(iterable, separator, expected):
    assert join(iterable, separator) == expected

@pytest.mark.strings
@pytest.mark.join
@pytest.mark.parametrize("iterable,separator,not_expected", [("123", "+", "123"), ("123", "+", "123+"), ("123", " ", "123")])
def test_join_two(iterable, separator, not_expected):
    assert join(iterable, separator) != not_expected

@pytest.mark.strings
@pytest.mark.join
@pytest.mark.parametrize("iterable,separator", [(1232, "+")])
def test_join_three(iterable, separator):
    with pytest.raises(TypeError):
        join(iterable, separator)

@pytest.mark.strings
@pytest.mark.lower
@pytest.mark.parametrize("string,expected", [("HELLO", "hello"), ("Russell", "russell"), ("jocelYN", "jocelyn"), ("3432", "3432")])
def test_lower_one(string, expected):
    assert lower(string) == expected

@pytest.mark.strings
@pytest.mark.lower
@pytest.mark.parametrize("string,not_expected", [("HELLO", "HELLO"), ("russell", "RUSSELL"), ("Jocelyn", "jOCELYN")])
def test_lower_two(string, not_expected):
    assert lower(string) != not_expected

@pytest.mark.strings
@pytest.mark.lower
@pytest.mark.parametrize("string", [(4324)])
def test_lower_three(string):
    with pytest.raises(TypeError):
        lower(string)

@pytest.mark.strings
@pytest.mark.replace
@pytest.mark.parametrize("string,old_value,new_value,expected", [("hello", "ll", "rr", "herro"), ("the dog went to the park", "park", "kennel", "the dog went to the kennel"), ("hello", "34234", "3344", "hello")])
def test_replace_one(string, old_value, new_value, expected):
    assert replace(string, old_value, new_value) == expected

@pytest.mark.strings
@pytest.mark.replace
@pytest.mark.parametrize("string,old_value,new_value,not_expected", [("hello", "ll", "rr", "hello"), ("hello", "ll", "rr", "rr"), ("the dog went to the park", "park", "kennel", "the dog with to the park")])
def test_replace_two(string, old_value, new_value, not_expected):
    assert replace(string, old_value, new_value) != not_expected

@pytest.mark.strings
@pytest.mark.replace
@pytest.mark.parametrize("string,old_value,new_value", [(34324, 232, 3423)])
def test_replace_three(string, old_value, new_value):
    with pytest.raises(TypeError):
        replace(string, old_value, new_value)

@pytest.mark.strings
@pytest.mark.split
@pytest.mark.parametrize("string,separator,expected", [("the dog went to the park", " ", ["the", "dog", "went", "to", "the", "park"]), ("hello", "l", ["he", "", "o"])])
def test_split_one(string, separator, expected):
    assert split(string, separator) == expected

@pytest.mark.strings
@pytest.mark.split
@pytest.mark.parametrize("string,separator,not_expected", [("the dog went to the park", " ", "the dog went to the park"), ("hello", " ", ["h", "e", "l", "l", "o"])])
def test_split_two(string, separator, not_expected):
    assert split(string, separator) != not_expected

@pytest.mark.strings
@pytest.mark.split
@pytest.mark.parametrize("string,separator,error", [("hello", "", ValueError), (23321, " ", TypeError)])
def test_split_three(string, separator, error):
    with pytest.raises(error):
        split(string, separator)

@pytest.mark.strings
@pytest.mark.title
@pytest.mark.parametrize("string,expected", [("hello", "Hello"), ("the dog went to the park", "The Dog Went To The Park"), ("hello b2b2b2", "Hello B2B2B2")])
def test_title_one(string, expected):
    assert title(string) == expected

@pytest.mark.strings
@pytest.mark.title
@pytest.mark.parametrize("string,not_expected", [("hello", "hello"), ("the dog went to the park", "The dog went to the park"), ("hello b2b2b2", "Hello B2b2b2")])
def test_title_two(string, not_expected):
    assert title(string) != not_expected

@pytest.mark.strings
@pytest.mark.title
@pytest.mark.parametrize("string", [(22222)])
def test_title_three(string):
    with pytest.raises(TypeError):
        title(string)