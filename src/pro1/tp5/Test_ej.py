import pytest
from functions import *


@pytest.mark.parametrize("a,res", [(5, 10)])
def test_ejs(a, res):
    # Ejercicio 11 | crear una funcion propia
    assert sumar_cinco(a) == res


@pytest.mark.parametrize("a,res", [("juan", {1: "j", 2: "u", 3: "a", 4: "n"})])
def test_ejWord(a, res):
    assert word_dictionary(a) == res


@pytest.mark.parametrize("a,res", [(7, True)])
def test_ejPrimo(a, res):
    assert es_primo(a) == res


@pytest.mark.parametrize("a,res", [(4, 24)])
def test_ejFactorial(a, res):
    assert factorial(a) == res


@pytest.mark.parametrize("a,b,res", [(1223, 2, 2)])
def test_ejContadorDigitos(a, b, res):
    assert compare_digits(a, b) == res
