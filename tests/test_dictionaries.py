from typing import Type
import pytest
from ..src.dictionaries import *

@pytest.mark.dictionaries
@pytest.mark.clear_d
@pytest.mark.parametrize("dic,expected", [({"hello": "hi"}, {}), ({"one": 1, "two": 2}, {}), ({"one": True, "two": {"one": 1}, "three": [1,2,3]}, {})])
def test_clear_one(dic, expected):
    assert clear(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.clear_d
def test_clear_two():
    dic = {}
    dicID = id(dic)
    assert id(clear(dic)) == dicID

@pytest.mark.dictionaries
@pytest.mark.clear_d
def test_clear_three():
    with pytest.raises(TypeError):
        clear([1,2,3])

@pytest.mark.dictionaries
@pytest.mark.copy_d
@pytest.mark.parametrize("dic,expected", [({"one":1}, {"one":1}), ({"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}}, {"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}})])
def test_copy_one(dic, expected):
    assert copy(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.copy_d
@pytest.mark.parametrize("dic", [({"one":1}), ({"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}})])
def test_copy_two(dic):
    dicID = id(dic)
    assert id(copy(dic)) != dicID

@pytest.mark.dictionaries
@pytest.mark.copy_d
def test_copy_three():
    with pytest.raises(TypeError):
        copy([1,2,3])

@pytest.mark.dictionaries
@pytest.mark.get
@pytest.mark.parametrize("dic,key,value,expected", [({"one": 1}, "one", None, 1), ({"russell": "amazing"}, "jocelyn", "lame", "lame")])
def test_get_one(dic, key, value, expected):
    assert get(dic, key, value) == expected

@pytest.mark.dictionaries
@pytest.mark.get
def test_get_two():
    with pytest.raises(TypeError):
        get([1,2,3], "1")

@pytest.mark.dictionaries
@pytest.mark.items
@pytest.mark.parametrize("dic, expected", [({"one": 1, "two": 2, "three": 3}, [("one", 1), ("two", 2), ("three", 3)]), ({"dog": {"name": "woof"}, "cat": {"name": "meow"}}, [("dog", {"name": "woof"}), ("cat", {"name": "meow"})])])
def test_items_one(dic, expected):
    assert items(dic) == expected