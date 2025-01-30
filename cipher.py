
def translate(from_letters, to_letters, text):
    """
    The translate function does a letter to letter translation.
    The from_letters and to_letters parameters are expected to
    be strings of uppercase letters and both strings need to be 
    the same length. The from_letters and to_letters strings define
    a mapping such that from_letters[i] found in the text string 
    parameter will be converted to to_letters[i].  All characters in 
    the text parameter not found in from_letters are left as-is.
    Case of letters in the text parameter are preserved in the result.
    For example translate("ABC","CAB","C3PO-aBA") will return the 
    string "B3PO-cAC".  Likewise, translate("CAB","ABC","B3PO-cAC")
    will return the string "C3PO-aBA".   
    """ 

    # Check that parameters meet assumptions. The only assumption not
    # tested is that each character in from_letters should occur once.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # code below is the translate function logic

    output = ""

    for i in range(len(text)):
        if not text[i].isalpha():
            output += text[i]
        else:
            for j in range(len(from_letters)):
                if text[i].upper() == from_letters[j]:
                    if text[i].isupper():
                        output += to_letters[j]
                    else:
                        output += to_letters[j].lower()

    return output

def main():

    with open("commands.txt", "r") as f:
        file_key = f.readline().strip()
        job_type = f.readline().strip()
        file_input = f.readline().strip()
        file_output = f.readline().strip()

    with open(file_input, "r") as f:
        input = f.readline().strip()

    with open(file_key, "r") as f:
        key = f.readline().strip()
        alphabet = f.readline().strip()

    with open(file_output, "w") as f:
        if job_type == "encrypt":
            f.write(translate(key, alphabet, input))
        else:
            f.write(translate(alphabet, key, input))

if __name__ == "__main__":
    main()
