import pytest
from ..src.dictionaries import *

@pytest.mark.dictionaries
@pytest.mark.clear_d
@pytest.mark.parametrize("dic,expected", [({"hello": "hi"}, {}), ({"one": 1, "two": 2}, {}), ({"one": True, "two": {"one": 1}, "three": [1,2,3]}, {})])
def test_clear_one(dic, expected):
    assert clear_d(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.clear_d
def test_clear_two():
    dic = {}
    dicID = id(dic)
    assert id(clear_d(dic)) == dicID

@pytest.mark.dictionaries
@pytest.mark.clear_d
def test_clear_three():
    with pytest.raises(TypeError):
        clear_d([1,2,3])

@pytest.mark.dictionaries
@pytest.mark.copy_d
@pytest.mark.parametrize("dic,expected", [({"one":1}, {"one":1}), ({"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}}, {"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}})])
def test_copy_one(dic, expected):
    assert copy_d(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.copy_d
@pytest.mark.parametrize("dic", [({"one":1}), ({"person": {"name": "jocelyn", "gender": "female", "likes": ["programming", "looking pretty", "Russell", "vintage"]}})])
def test_copy_two(dic):
    dicID = id(dic)
    assert id(copy_d(dic)) != dicID

@pytest.mark.dictionaries
@pytest.mark.copy_d
def test_copy_three():
    with pytest.raises(TypeError):
        copy_d([1,2,3])

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
@pytest.mark.parametrize("dic, expected", [({"one": 1, "two": 2, "three": 3}, [("one", 1), ("two", 2), ("three", 3)]), ({"dog": {"name": "woof"}, "cat": {"name": "meow"}}, [("dog", {"name": "woof"}), ("cat", {"name": "meow"}), ({}, [])])])
def test_items_one(dic, expected):
    assert items(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.items
def test_items_two():
    with pytest.raises(TypeError):
        items([])

@pytest.mark.dictionaries
@pytest.mark.pop_d
@pytest.mark.parametrize("dic,key,defaultvalue,expected", [({"one": 1}, "one", None, ({}, 1)), ({"name": "Russell", "height": 176, "weight": 70}, "eye-color", None, (None, {"name": "Russell", "height": 176, "weight": 70}))])
def test_pop_one(dic, key, defaultvalue, expected):
    assert pop_d(dic, key, defaultvalue) == expected

@pytest.mark.dictionaries
@pytest.mark.pop_d
@pytest.mark.parametrize("dic,key,expected_exception", [({"one":1}, "two", KeyError), (["one","two","three"], "two", TypeError)])
def test_pop_two(dic, key, expected_exception):
    with pytest.raises(expected_exception):
        pop_d(dic, key)

@pytest.mark.dictionaries
@pytest.mark.pop_d
def test_pop_three():
    dic = {"one": 1}
    dicID = id(dic)
    assert id(pop_d(dic, "one")[0]) == dicID

@pytest.mark.dictionaries
@pytest.mark.update
@pytest.mark.parametrize("dic,iterable,expected", [({"one": 1}, {"two": 2, "three": 3}, {"one": 1, "two": 2, "three": 3}), ({"one": 1}, {"one": "one"}, {"one": "one"})])
def test_update_one(dic, iterable, expected):
    assert update(dic, iterable) == expected

@pytest.mark.dictionaries
@pytest.mark.update
def test_update_two():
    dic = {"one": 1}
    dicID = id(dic)
    assert id(update(dic, {"two": 2})) == dicID

@pytest.mark.dictionaries
@pytest.mark.update
@pytest.mark.parametrize("dic,iterable,expected_exception", [({"one": 1}, ["two"], ValueError), (["one"], {"two": 2}, TypeError)])
def test_update_three(dic, iterable, expected_exception):
    with pytest.raises(expected_exception):
        update(dic, iterable)

@pytest.mark.dictionaries
@pytest.mark.values
@pytest.mark.parametrize("dic,expected", [({"one": 1}, [1]), ({"person": {"name": "jocelyn", "height": "short", "nationality": "malayasia"}}, [{"name": "jocelyn", "height": "short", "nationality": "malayasia"}]), ({}, [])])
def test_values_one(dic, expected):
    assert values(dic) == expected

@pytest.mark.dictionaries
@pytest.mark.values
def test_values_two():
    with pytest.raises(TypeError):
        values([1,2,3])