import hashlib
import time

def compute_file_hash(filename):
    """Generates a base SHA-256 hash of a file's contents."""
    sha = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

def mine_proof_of_work(target_zeros=4):
    print("⏳ Reading license files to construct block header...")
    eula_hash = compute_file_hash("EULA.md")
    cloudflare_hash = compute_file_hash("CLOUDFLARE_TERMS.md")
    
    # Combine your data files into a single cryptographic block string
    block_data = f"{eula_hash}:{cloudflare_hash}"
    target_prefix = "0" * target_zeros
    
    nonce = 0
    start_time = time.time()
    print(f"🚀 Mining Block... Target difficulty: {target_zeros} leading zeros.")
    
    while True:
        # Append the nonce to the data string to vary the output hash
        payload = f"{block_data}:{nonce}".encode('utf-8')
        block_hash = hashlib.sha256(payload).hexdigest()
        
        # Check if the hash matches our Proof of Work difficulty constraint
        if block_hash.startswith(target_prefix):
            elapsed = time.time() - start_time
            print("\n👑 PROOF OF WORK VERIFIED!")
            print(f"Nonce Found : {nonce}")
            print(f"Block Hash  : {block_hash}")
            print(f"Time Taken  : {elapsed:.2f} seconds")
            
            # Save the valid block data as your verifiable transaction receipt
            with open("pow_receipt.txt", "w") as r:
                r.write(f"BLOCK_HASH: {block_hash}\nNONCE: {nonce}\nDIFFICULTY: {target_zeros}\n")
            break
            
        nonce += 1
        if nonce % 100000 == 0:
            print(f"⛏️  Hashed {nonce} nonces... still mining...", end="\r")

if __name__ == "__main__":
    mine_proof_of_work(target_zeros=4) # Change number to scale up difficulty
