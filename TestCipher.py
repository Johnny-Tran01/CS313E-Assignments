#  File: TestCipher.py

#  Description:

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/1/2022

#  Date Last Modified:

import sys


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    key = int(key)
    rail_2d = [['-' for col in range(len(strng))] for row in range(key)]
    direction = False
    row_num = 0
    col_num = 0
    encoded = ''

    for char in strng:
        if row_num == 0 or row_num == key - 1:
            direction = not direction
        rail_2d[row_num][col_num] = char
        col_num += 1
        if direction:
            row_num += 1
        else:
            row_num -= 1

    for row in range(key):
        for col in range(len(strng)):
            if rail_2d[row][col] != '-':
                encoded += (rail_2d[row][col])

    return encoded  # placeholder for the actual return statement


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    key = int(key)
    rail_2d = [['-' for col in range(len(strng))] for row in range(key)]
    direction = False
    row_num = 0
    col_num = 0
    char_pos = 0
    decoded = ''

    for char in strng:
        if row_num == 0 or row_num == key - 1:
            direction = not direction
        rail_2d[row_num][col_num] = '!'
        col_num += 1
        if direction:
            row_num += 1
        else:
            row_num -= 1

    for row in range(key):
        for col in range(len(strng)):
            if rail_2d[row][col] == '!':
                rail_2d[row][col] = strng[char_pos]
                char_pos += 1

    row_num = 0
    col_num = 0
    direction = False
    for char in strng:
        if row_num == 0 or row_num == key - 1:
            direction = not direction
        decoded += (rail_2d[row_num][col_num])
        col_num += 1
        if direction:
            row_num += 1
        else:
            row_num -= 1

    return decoded  # placeholder for the actual return statement


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    new_string = ''
    lowered_string = strng.lower()
    for i in range(len(lowered_string)):
        if lowered_string[i].isalpha():
            new_string += lowered_string[i]
    return new_string  # placeholder for the actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    p_value = ord(p) - ord('a')
    s_value = ord(s) - ord('a')
    character = chr(ord('a') + (p_value + s_value) % 26)
    return character  # placeholder for actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    p_value = ord(p) - ord('a')
    s_value = ord(s) - ord('a')
    character = chr(ord('a') + abs(s_value - p_value + 26) % 26)
    return character  # placeholder for actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    encoded = ''
    for i in range(len(strng)):
        encoded += encode_character(phrase[i % len(phrase)], strng[i])
    return encoded  # placeholder for the actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    decoded = ''
    for i in range(len(strng)):
        decoded += decode_character(phrase[i % len(phrase)], strng[i])
    return decoded  # placeholder for the actual return statement


def main():
    # read the plain text from stdin
    rail_encode_text = sys.stdin.readline().strip()
    print('Plain Text: ' + rail_encode_text)
    # read the key from stdin
    encode_key = sys.stdin.readline().strip()
    print('Key: ' + encode_key)
    # encrypt and print the encoded text using rail fence cipher
    print('Encoded Text: ' + rail_fence_encode(rail_encode_text, encode_key)
          + '\n')
    # read encoded text from stdin
    rail_decode_text = sys.stdin.readline().strip()
    print('Encoded Text: ' + rail_decode_text)
    # read the key from stdin
    decode_key = sys.stdin.readline().strip()
    print('Key: ' + decode_key)
    # decrypt and print the plain text using rail fence cipher
    print('Decoded Text: ' + rail_fence_decode(rail_decode_text,
                                               decode_key) + '\n')
    # read the plain text from stdin
    vig_encode_text = sys.stdin.readline().strip()
    print('Plain Text: ' + vig_encode_text)
    # read the pass phrase from stdin
    encode_pass = sys.stdin.readline().strip()
    print('Pass Phrase: ' + encode_pass)
    # encrypt and print the encoded text using Vigenere cipher
    print('Encoded Text: ' + vigenere_encode(vig_encode_text, encode_pass) +
          '\n')
    # read the encoded text from stdin
    vig_decode_text = sys.stdin.readline().strip()
    print('Encoded Text: ' + vig_decode_text)
    # read the pass phrase from stdin
    decode_pass = sys.stdin.readline().strip()
    print('Pass Phrase: ' + decode_pass)
    # decrypt and print the plain text using Vigenere cipher
    print('Decoded Text: ' + vigenere_decode(vig_decode_text, decode_pass))


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
