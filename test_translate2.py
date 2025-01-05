from cipher import translate

def test_translate_multiple_letters_and_numbers():
    assert translate("ABC","BCA","ABC1AA2B") == "BCA1BB2C"

def test_translate_multiple_letters_and_numbers_and_whitespace():
    assert translate("ABC","BCA","ABC1 AA2B\n") == "BCA1 BB2C\n"

def test_translate_as_cipher_with_spaces_and_numbers_and_punctuation():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "JIOCANTRQWUKVEGXPDFZBMHLSY"
    text = "MSCI 121!"
    expected_results = "VFOQ 121!"
    assert translate(alphabet,key,text) == expected_results

    