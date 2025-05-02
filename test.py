import pandas as pd
import numpy as np
import pickle
from config import BLD, test_dict, encrypted_message

test_zeros = np.zeros(10)
test_df = pd.DataFrame(test_zeros, columns=['test'])

def decode_message(decryption_dict:dict, encrypted_message:list):
    message = ''
    for i in encrypted_message:
        message += decryption_dict[i]
    return message

if __name__ == '__main__':
    target_path = BLD
    if not target_path.is_dir():
        target_path.mkdir(exist_ok=True, parents=True)

    message = decode_message(test_dict, encrypted_message)

    with open(target_path / 'test.pkl', "wb") as f:
        pickle.dump(message, f)

    with open(target_path / 'test.pkl', "rb") as f:
        message = pickle.load(f)

    print(message, flush=True)