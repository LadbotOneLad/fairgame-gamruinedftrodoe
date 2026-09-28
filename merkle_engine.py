import hashlib
import json

# The exact 14 calculated fingerprints from your output buffer
nodes = [
    "195b5d97a55098238e2b9cdf",
    "7ac19521af6d2510aee0b737",
    "ce30a245badd4fb0fae5f4f2",
    "e34516c62328ec4a953d96ad",
    "9e7c00dc26faf367fc181fa3",
    "bf10cd2f60fb61faf423055b",
    "8d3d534e3d9dac8dd8f24579",
    "6e31bbd342844269b08faa82",
    "896415d72f7ca7dd250f0465",
    "df92cdd58eb7af953535b663",
    "4b8cf78335b6ae4e47aecbdc",
    "c4cff5f8f2ea0a4eba0fa31e",
    "6860b541426f35c00004db88",
    "0bb0d8a3cb7179da9e56a269"
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

print(f"[+] TRUE MERKLE TREE SYNTHESISED")
print(f"[!] HIERARCHICAL ROOT: {root_hash}")
