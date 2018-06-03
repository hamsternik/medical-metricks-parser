__author__ = 'khomitsevich'

import string

ENGLISH_ALPHABET_LIST = list(string.ascii_uppercase)
ENGLISH_ALPHABET_LIST_LEN = len(ENGLISH_ALPHABET_LIST)

def get_excel_char_index_by_numeric(num_index:int):
    if num_index // ENGLISH_ALPHABET_LIST_LEN == 0:
        return ENGLISH_ALPHABET_LIST[num_index]
    elif num_index // ENGLISH_ALPHABET_LIST_LEN <= 26:
        trailing_chr_index = (num_index // ENGLISH_ALPHABET_LIST_LEN) - 1
        trailing_chr = ENGLISH_ALPHABET_LIST[trailing_chr_index]    
        leading_chr_index = num_index % ENGLISH_ALPHABET_LIST_LEN
        leading_chr = ENGLISH_ALPHABET_LIST[leading_chr_index]
        return trailing_chr + leading_chr
    return None
