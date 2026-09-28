import hashlib
import json

# Fetch hashes from your 14 nodes
nodes = [
    "5d41402abc4b2a76b9719d911017c592", # Dummy placeholders representing your computed vectors
    "7d41402abc4b2a76b9719d911017c593",
    "8d41402abc4b2a76b9719d911017c594",
    "9d41402abc4b2a76b9719d911017c595",
    "0d41402abc4b2a76b9719d911017c596",
    "1d41402abc4b2a76b9719d911017c597",
    "2d41402abc4b2a76b9719d911017c598",
    "3d41402abc4b2a76b9719d911017c599",
    "4d41402abc4b2a76b9719d911017c600",
    "5d41402abc4b2a76b9719d911017c601",
    "6d41402abc4b2a76b9719d911017c602",
    "7d41402abc4b2a76b9719d911017c603",
    "8d41402abc4b2a76b9719d911017c604",
    "9d41402abc4b2a76b9719d911017c605"
]

def hash_pair(a, b):
    return hashlib.sha256((a + b).encode('utf-8')).hexdigest()

def build_merkle_tree(leaves):
    tree = [leaves]
    while len(leaves) > 1:
        next_level = []
        for i in range(0, len(leaves), 2):
            if i + 1 < len(leaves):
                next_level.append(hash_pair(leaves[i], leaves[i+1]))
            else:
                # Odd node duplication mapping
                next_level.append(hash_pair(leaves[i], leaves[i]))
        leaves = next_level
        tree.append(leaves)
    return tree

tree = build_merkle_tree(nodes)
root_hash = tree[-1][0]

manifest = {
    "version": "1.0.0",
    "identity": "ATOM-TRUTH-GENESIS",
    "merkle_root": root_hash,
    "tree_depth": len(tree) - 1,
    "leaves_count": len(nodes)
}

with open("merkle_manifest.json", "w") as f:
    json.dump(manifest, f, indent=4)

print(f"[+] MERKLE TREE SYNTHESISED SUCCESSFULLY")
print(f"[!] GLOBAL ROOT HASH: {root_hash}")
