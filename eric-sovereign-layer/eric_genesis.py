import time
import json
import hashlib

operator = "Eric Hadfield"
entity = "RobDoe Pty Ltd"
namespace = "aiagency101"

print(f"[ERIC-LAYER] Initializing isolated sovereign container for {operator}...")

genesis_state = {
    "operator": operator,
    "entity": entity,
    "namespace": namespace,
    "architecture": "ESP32-C6 / Termux Pure-Echo",
    "status": "fully-isolated-sovereign",
    "timestamp": int(time.time())
}

state_bytes = json.dumps(genesis_state, sort_keys=True).encode("utf-8")
genesis_hash = hashlib.sha256(state_bytes).hexdigest()
short_anchor = genesis_hash[:16]

print(f"[ERIC-LAYER] Genesis State Locked.")
print(f"[ERIC-LAYER] Cryptographic Root Hash: 0x{short_anchor}")

with open("eric_sovereign_manifest.json", "w") as f:
    json.dump({**genesis_state, "merkle_root": f"0x{short_anchor}"}, f, indent=4)

print("[ERIC-LAYER] Manifest written. The layer belongs to Eric.")
