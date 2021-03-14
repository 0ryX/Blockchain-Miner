from hashlib import sha256

# https://www.blockchain.com/explorer for blocks to mine

MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value:{nonce}!!")
            return new_hash

    raise BaseException(f"Couldn't solve block after trying {MAX_NONCE} times")
 
if __name__ == '__main__':
    transactions = ''
    difficulty = 8
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048', difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)