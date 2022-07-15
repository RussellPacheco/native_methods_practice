from typing import Type
import pytest
from ..src.lists import *

@pytest.mark.lists
@pytest.mark.append
@pytest.mark.parametrize("array,element,expected", [([1,2,3], 4, [1,2,3,4]), (["a", "b", "c"], "d", ["a", "b", "c", "d"]), ([{"one": 1},{"two": 2},{"three": 3}], {"four": 4}, [{"one": 1},{"two": 2},{"three": 3}, {"four": 4}])])
def test_append_one(array, element, expected):
    assert append(array, element) == expected

@pytest.mark.lists
@pytest.mark.append
@pytest.mark.parametrize("array,element,not_expected", [([1,2,3], 3, "[1,2,3]3"), (["a", "b", "c"], "d", "a, b, c, d"), ([1,2,3], [4], [1,2,3,4])])
def test_append_two(array, element, not_expected):
    assert append(array, element) != not_expected

@pytest.mark.lists
@pytest.mark.append
def test_append_three():
    arr = [1,2,3]
    arrID = id(arr)
    assert id(append(arr, 4)) == arrID

@pytest.mark.lists
@pytest.mark.append
def test_append_four():
    with pytest.raises(TypeError):
        append({"one": "one"}, 12)

@pytest.mark.lists
@pytest.mark.clear
def test_clear_one():
    assert clear([1,2,3]) == []

@pytest.mark.lists
@pytest.mark.clear
def test_clear_two():
    arr = [1,2,3]
    arrID = id(arr)
    assert id(clear(arr)) == arrID

@pytest.mark.lists
@pytest.mark.clear
def test_clear_three():
    with pytest.raises(TypeError):
        clear({"one": 1})


@pytest.mark.lists
@pytest.mark.copy
def test_copy_one():
    assert copy([1,2,3]) == [1,2,3]

@pytest.mark.lists
@pytest.mark.copy
def test_copy_two():
    arr = [1,2,3]
    arrID = id(arr)
    assert id(copy(arr)) != arrID
    
@pytest.mark.lists
@pytest.mark.copy
def test_copy_three():
    with pytest.raises(TypeError):
        copy(2)

@pytest.mark.lists
@pytest.mark.count_l
@pytest.mark.parametrize("array,value,expected", [([2,2,2], 2, 3), (["a", "c", "a"], "a", 2)])
def test_count_one(array, value, expected):
    assert count(array, value) == expected

@pytest.mark.lists
@pytest.mark.count_l
def test_count_two():
    with pytest.raises(TypeError):
        count(24, 23)

@pytest.mark.lists
@pytest.mark.extend
@pytest.mark.parametrize("array,iterable,expected", [([1,2,3], [4,5,6], [1,2,3,4,5,6]), (["a", "b", "c"], "def", ["a", "b", "c", "d", "e", "f"])])
def test_extend_one(array, iterable, expected):
    assert extend(array, iterable) == expected

@pytest.mark.lists
@pytest.mark.extend
def test_extend_two():
    arr = [1,2,3]
    arrID = id(arr)
    assert id(extend(arr, [4,5,6])) == arrID

@pytest.mark.lists
@pytest.mark.extend
@pytest.mark.parametrize("array,iterable", [([1,2,3], 4), ("abc", ["d", "e", "f"])])
def test_extend_three(array, iterable):
    with pytest.raises(TypeError):
        extend(array, iterable)

@pytest.mark.lists
@pytest.mark.index_l
@pytest.mark.parametrize("array,value,expected", [([1,2,3], 3, 2), (["a","b","c"], "b", 1), (["a", "a", "c", "d", "c"], "c", 2)])
def test_index_one(array, value, expected):
    assert index(array, value) == expected

@pytest.mark.lists
@pytest.mark.index_l
@pytest.mark.parametrize("array,value,expected", [([1,2,3], 4, ValueError), ("123", "1", TypeError)])
def test_index_two(array, value, expected):
    with pytest.raises(expected):
        index(array, value)

@pytest.mark.lists
@pytest.mark.pop
@pytest.mark.parametrize("array,index,expected", [([1,2,3], -1, ([1,2], 3)), ([1,2,3], 0, ([1, 2], 1)), (["a", "b", "c"], 2, (["a", "b"], "c"))])
def test_pop_one(array, index, expected):
    assert pop(array, index) == expected

@pytest.mark.lists
@pytest.mark.pop
@pytest.mark.parametrize("array,index,expected_exception", [([1,2,3], 3, IndexError), ("1,2,3", 0, TypeError)])
def test_pop_two(array, index, expected_exception):
    with pytest.raises(expected_exception):
        pop(array, index)

@pytest.mark.lists
@pytest.mark.remove
@pytest.mark.parametrize("array,value,expected", [([1,2,3], 1, [2,3]), (["a", "b", "c"], "b", ["a", "c"])])
def test_remove_one(array, value, expected):
    assert remove(array, value) == expected

@pytest.mark.lists
@pytest.mark.remove
@pytest.mark.parametrize("array,value,expected_exception", [([1,2,3], 4, ValueError), ("123", 3, TypeError)])
def test_remove_two(array, value, expected_exception):
    with pytest.raises(expected_exception):
        remove(array, value)

@pytest.mark.lists
@pytest.mark.reverse
@pytest.mark.parametrize("array,expected", [([1,2,3], [3,2,1]), (["a", "b", "c"], ["c", "b", "a"]), ([], [])])
def test_reverse_one(array, expected):
    assert reverse(array) == expected

@pytest.mark.lists
@pytest.mark.reverse
def test_reverse_two():
    arr = [1,2,3]
    arrID = id(arr)
    assert id(reverse(arr)) == arrID

@pytest.mark.lists
@pytest.mark.reverse
def test_reverse_three():
    with pytest.raises(TypeError):
        reverse("abc")

@pytest.mark.lists
@pytest.mark.sort
@pytest.mark.parametrize("array,reverse,expected", [([1,3,2], False, [1,2,3]), (["d", "c", "a"], False, ["a", "c", "d"]), (["a", "b", "c"], True, ["c", "b", "a"])])
def test_sort_one(array, reverse, expected):
    assert sort(array, reverse) == expected

@pytest.mark.lists
@pytest.mark.sort
def test_sort_two():
    arr = [1,2,3]
    arrID = id(arrID)
    assert id(sort(arr)) == arrID

@pytest.mark.lists
@pytest.mark.sort
def test_sort_three():
    with pytest.raises(TypeError):
        sort({"one": 1, "two": 2})