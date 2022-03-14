
import numpy


# Start of Helper Functions
def box(m):
    m = m.lower()  # converting lowercase
    arr = [0] * len(m)  # initializing array with same length as the length
    i = 0
    for n in m:
        if not ('a' <= n <= 'z'):  # excluding special characters
            continue
        arr[i] = (ord(n) - ord('a'))  # subtracting ascii character values by a so we can map it to 0-25
        i += 1
    arr_f = arr[0:i]  # array final - to exclude the special character in the array
    return arr_f


def unbox(enc_f):
    m = ""
    for x in enc_f:
        m += chr(x + ord('a'))
    return m.upper()


def row_trans_enc(plaintext,k):  # Your encryption function should have the same name and must accept a string as plaintext and key
    m = box(plaintext)
    x = unbox(m)
    lex = len(x)
    arr_k = list(k)
    arr_key = [int(i) for i in arr_k]
    lek = len(arr_key)
    pad = lek - (lex % lek)
    Ptext = x + pad * 'X'
    arr_p = list(Ptext)
    keyarray = numpy.argsort(
        arr_key)  # Returns the indices that would sort an array. Instead of using just sort because we are working with indices

    ciphertext = ""
    for c in keyarray:
        for r in range(int(len(arr_p) / lek)):  # making array
            ciphertext += Ptext[(r * lek) + c]  # appending ciphertext

    return ciphertext  # Your function must return a string

def row_trans_dec(ciphertext, k): # similar to enc but some changes to make it dec
    m = box(ciphertext)
    x = unbox(m)
    letters = list(ciphertext)
    lex = len(letters)

    arr_k = list(k)
    arr_k = [int(x) for x in arr_k]
    kLen = len(arr_k)

    lexc = int(lex / kLen)

    plaintext = ""
    for i in range(lexc):
        for j in arr_k:
            k = (lexc * (j - 1)) + i
            plaintext += ciphertext[k]
    return plaintext


s