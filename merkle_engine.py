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
# --- MERKLE DAG INTEGRITY & AINTEGRATION ENGINE ---
import os
import hashlib
import json
from datetime import datetime

ROOT_DIR = os.path.expanduser("~/robdoerootauthority")
LEDGER_FILE = os.path.join(ROOT_DIR, "STATE_PROOFS.jsonl")

def hash_content(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def get_latest_merkle_root():
    if not os.path.exists(LEDGER_FILE):
        return "GENESIS_ROOT_E14F9A8D"
    
    last_hash = ""
    with open(LEDGER_FILE, "r") as f:
        for line in f:
            try:
                record = json.loads(line.strip())
                last_hash = record.get("merkle_hash", last_hash)
            except:
                pass
    return last_hash if last_hash else "GENESIS_ROOT_E14F9A8D"

def append_dag_node(event_type: str, details: str):
    parent_hash = get_latest_merkle_root()
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    payload = f"{timestamp}|{parent_hash}|{event_type}|{details}"
    current_hash = hash_content(payload)
    
    node_record = {
        "timestamp": timestamp,
        "parent_merkle_hash": parent_hash,
        "event_type": event_type,
        "details": details,
        "merkle_hash": current_hash
    }
    
    os.makedirs(ROOT_DIR, exist_ok=True)
    with open(LEDGER_FILE, "a") as f:
        f.write(json.dumps(node_record) + "\n")
        
    print(f"[MERKLE DAG] Integrated -> Type: {event_type} | Hash: {current_hash[:12]}...")

if __name__ == "__main__":
    append_dag_node("DAG_INTEGRATION", "Master daemon parallel chaos launcher synchronized with Merkle DAG tree.")
