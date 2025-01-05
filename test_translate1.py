from cipher import translate
import pytest

def test_translate_arguments():
    """
    This test the checks catching arugment errors. 
    Students can ignore this test. If this test fails,
    it means that students have deleted some provided
    code from translate and should put it back.
    """
    with pytest.raises(ValueError):
        translate("abc","BCA","bbb") # from_letter is not all upper
    with pytest.raises(ValueError):
        translate("ABC","bCA","BBB") # to_letters is not all upper
    with pytest.raises(ValueError):
        translate("ABC","BCAA","BBB") # diff lengths
    with pytest.raises(ValueError):
        translate("1BC","BCA","BBB") # not all letters
    with pytest.raises(ValueError):
        translate("ABC","B2A","BBB") # not all letters
    with pytest.raises(TypeError):
        translate("ABC","BCA",["b"])


def test_translate_one_letter():
    assert translate("A","B","A") == "B"


def test_translate_multiple_letters():
    assert translate("ABC","BCA","ABCAAB") == "BCABBC"


def test_translate_as_cipher():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "JIOCANTRQWUKVEGXPDFZBMHLSY"
    text = "MSCI"
    expected_results = "VFOQ"
    assert translate(alphabet,key,text) == expected_results

