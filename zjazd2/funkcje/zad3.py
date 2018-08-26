import pytest


def zlicz_znaki(text, start='<', end='>'):
    if start == end:
        raise ValueError("parametry start i end nie moga byc takie same!!!")
    count = 0
    level = 0
    for i in text:
        if i == start:
            level += 1
        elif i == end:
            level -= 1
        elif level >= 1:
            count += 1*level
    return count

def test_zlicz_znaki():
    assert zlicz_znaki("", ) == 0
    assert zlicz_znaki("ala ma <kota>, a kot ma ale") == 4
    assert zlicz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert zlicz_znaki('a <a<a<a>>>') == 6

def test_with_error():
    with pytest.raises(ValueError):
        zlicz_znaki("AAA", '.', '.')