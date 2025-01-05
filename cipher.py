
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
    # Students should not change this code.  It is here to catch mistakes.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Students should add their code below for the translate function

    txt = list(text)
    output = ""

    for i in range(len(txt)):
        for j in range(len(from_letters)):
            if str(txt[i]).isalpha():
                if str(text[i]).isupper() and str(text[i]) == from_letters[j].upper():
                    txt[i] = to_letters[j].upper()
                elif str(text[i]).islower() and str(text[i]) == from_letters[j].lower():
                    txt[i] = to_letters[j].lower()

        output += txt[i]

    return output

def main():

    input = open("input.txt")
    parameters = open("commands.txt")
    cmds = []

    for line in parameters:
        cmds.append(line)

    decrpyt = open("output.txt", "a")
    decrpyt.write(translate(input.readline(), cmds[0], cmds[1]))

    input.close()
    parameters.close()
    decrpyt.close()


if __name__ == "__main__":
    main()
