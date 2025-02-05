# Substitutive Cipher

## Overview
This program implements a simple **Substitution Cipher** for encrypting and decrypting text files based on a predefined key. The key provides a mapping of each letter of the alphabet to another letter, preserving the case of letters while keeping non-alphabetic characters unchanged.

## Learning Objectives
- Design and implement functions to solve small problems.
- Verify the correctness of a function by writing unit tests.
- Use decomposition to design and implement programs for solving complex problems.

## Process
- Reads a `commands.txt` file that specifies:
  1. The key file containing the encryption/decryption key.
  2. Whether to `encrypt` or `decrypt`.
  3. The input file to be processed.
  4. The output file where the result is stored.
- Preserves case sensitivity while ensuring non-alphabetic characters remain unchanged.
- Stores the result in the output file.

## Constraints
- To **not** use python's built in `translate()` or `maketrans()` methods.
- To **not** use dictionaries, maps, or hash tables.
- Assume that `commands.txt`, the input file, and the key file always exist.
- Assume the output file is different from the input file and may be overwritten.

## File Structure
```
├── README.md            # Project documentation (this file)
├── cipher.py            # Main program for encryption and decryption
├── commands.txt         # Specifies the key file, mode, input, and output files
├── input.txt            # File to be encrypted/decrypted
├── key.txt              # Encryption key (26 uppercase letters)
├── output.txt           # Output file with processed text
├── test_translate1.py   # Unit tests for initial translation function
├── test_translate2.py   # Unit tests with non-alphabetic characters
├── test_translate3.py   # Unit tests ensuring case sensitivity
```

## Program Execution
To run the program, ensure `commands.txt` is correctly formatted, then execute:
```sh
cipher.py
```
To run unit tests:
```sh
pytest --verbose test_translate1.py test_translate2.py test_translate3.py
```

## Lisence
This project is for educational purposes only and is open for use 
