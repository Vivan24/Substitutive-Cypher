from cipher import translate

def test_translate_multiple_letters_and_numbers_mixed_case():
    assert translate("ABC","BCA","AbC1Aa2B") == "BcA1Bb2C"

def test_translate_multiple_letters_and_numbers_and_whitespace_mixed_case():
    assert translate("ABC","BCA","aBC1 AA2b\n") == "bCA1 BB2c\n"

def test_translate_as_encrypt():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "JIOCANTRQWUKVEGXPDFZBMHLSY"
    text = "MSCI 121 is the best!\n"
    expected_results = "VFOQ 121 qf zra iafz!\n"
    assert translate(alphabet,key,text) == expected_results

def test_translate_as_decrypt():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "JIOCANTRQWUKVEGXPDFZBMHLSY"
    text = "VFOQ 121 qf zra iafz!\n"
    expected_results = "MSCI 121 is the best!\n"
    assert translate(key,alphabet,text) == expected_results
