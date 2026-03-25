import funkcje
import pytest

def test_add():
    assert funkcje.add(2,4) == 6
    assert not funkcje.add(2,4) == 5

def test_is_palindrom():
    assert funkcje.is_palindrom("kamilslimak") == True
    assert funkcje.is_palindrom("ala")
    assert funkcje.is_palindrom("wiadro") == False
    assert not funkcje.is_palindrom("kamyk")

def test_is_valid_triangle():
    assert funkcje.is_valid_triangle(2,3,4)
    assert funkcje.is_valid_triangle(4,6,7)

def test_invalid_triangle():
    assert not funkcje.is_valid_triangle(5,5,15)
    assert not funkcje.is_valid_triangle(-5,10,11)

def test_divide(capsys):
    funkcje.divide(4,2)
    out, err = capsys.readouterr()
    assert out == "2.0\n"