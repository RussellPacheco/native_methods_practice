from typing import Optional, Iterable, Type

def capitalize(string: str) -> str:
    #Convert the first character to uppercase
    if type(string) != str:
        raise TypeError
    return string[0].upper() + string[1:]


def center(string: str, length: int, character: Optional[str]) -> str:
    #Return a centered string in the specified length with the
    #optional specified character as the fill character  
    pass
def count(string: str, value: str, start: Optional[int], end: Optional[int]) -> int:
    #Return the number of times a specified value occurs in a string
    pass
def index(string: str, value: str, start: Optional[int], end: Optional[int]) -> int:
    #Search string for specified value and return the position of where it was found
    pass
def islower(string: str) -> bool:
    #Return true if all characters are lowercase
    pass
def isnumeric(string: str) -> str:
    #Return true if all characters in the string are numeric
    pass

# def join(separator: str, iterable: Iterable) -> str:
#     #Convert all elements of an iterable into a string
#     pass

def lower(string: str) -> str:
    #Convert a string into lowercase
    pass
def replace(string: str, old_value:str, new_value: str, count: Optional[int] ) -> str:
    #Return a new string where a specified value is replaced with a specified value
    pass
def split(string: str, separator: str) -> list:
    #Split the string at the specified separator and return a list
    pass
def title(string: str) -> str:
    #Convert the first character of each word to uppercase
    pass
