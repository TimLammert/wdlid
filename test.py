import pandas as pd
import numpy as np


test_zeros = np.zeros(10)
test_df = pd.DataFrame(test_zeros, columns=['test'])

def decode_message(decryption_dict:dict, encrypted_message:list):
    message = ''
    for i in encrypted_message:
        message += decryption_dict[i]
    return message

if __name__ == '__main__':

    encrypted_message = [23, 5, 18, 27, 4, 1, 19, 27, 12, 9, 5, 19, 20, 27, 9, 19, 20, 27, 4, 15, 15, 6, 28]
    test_dict = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z',
        27: ' ',
        28: '.'
    }

    message = decode_message(test_dict, encrypted_message)
    print(message, flush=True)