import os
import hashlib
import json

def get_file_sha256(filepath):
    h = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

# Target structural files in your GENESIS node
target_files = [
    "julia_ehf.py",
    "yinyang_matrix.py",
    "merkle_engine.py",
    "merkle_manifest.json"
]

print("[-] EXTRACTING DATA BLOB LEAVES...")
leaves = []

for filename in sorted(target_files):
    if os.path.exists(filename):
        f_hash = get_file_sha256(filename)
        leaves.append(f_hash)
        print(f"[*] Blob [{filename}] -> Leaf: {f_hash[:16]}...{f_hash[-8:]}")
    else:
        print(f"[!] Warning: Missing blob artifact [{filename}]")

def hash_pair(a, b):
    return hashlib.sha256((a + b).encode('utf-8')).hexdigest()

def process_merkle_layers(nodes):
    current_layer = nodes
    layer_idx = 0
    tree_map = {f"Layer_0_Leaves": current_layer}
    
    while len(current_layer) > 1:
        layer_idx += 1
        next_layer = []
        for i in range(0, len(current_layer), 2):
            if i + 1 < len(current_layer):
                next_layer.append(hash_pair(current_layer[i], current_layer[i+1]))
            else:
                next_layer.append(hash_pair(current_layer[i], current_layer[i]))
        current_layer = next_layer
        tree_map[f"Layer_{layer_idx}_Nodes"] = current_layer
        
    return current_layer[0], tree_map

if leaves:
    blob_root, complete_tree = process_merkle_layers(leaves)
    
    blob_manifest = {
        "engine": "MYWARE_BLOB_MERKLE_V2",
        "global_blob_root": blob_root,
        "structural_topology": complete_tree
    }
    
    with open("blob_merkle_manifest.json", "w") as f:
        json.dump(blob_manifest, f, indent=4)
        
    print(f"\n[+] RECURSIVE BLOB MERKLE INTEGRATION SUCCESSFUL")
    print(f"[!] GLOBAL BLOB ROOT: {blob_root}")
else:
    print("[!] Error: No valid blob files identified in runtime context.")
