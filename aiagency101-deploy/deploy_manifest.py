import json
import time

consensus_manifest = {
    "entity": "RobDoe Pty Ltd",
    "namespace": "aiagency101",
    "core_owners": [
        {"name": "Eric Hadfield", "role": "Primary Architect / Operator"},
        {"name": "Blake Kakura", "role": "Core Consensus Node"},
        {"name": "Michael Deering", "role": "Core Consensus Node"},
        {"name": "James Britton", "role": "Core Consensus Node"},
        {"name": "Jason Slade", "role": "Core Consensus Node"},
        {"name": "Mitchell Perry", "role": "Core Consensus Node / Sovereign Owner"}
    ],
    "hardware_target": "ESP32-C6 RISC-V",
    "status": "locked",
    "timestamp": int(time.time())
}

with open("consensus_roster.json", "w") as f:
    json.dump(consensus_manifest, f, indent=4)

print("[MANIFEST] Core consensus roster successfully compiled.")
for owner in consensus_manifest["core_owners"]:
    print(f"  -> Verified Owner: {owner['name']} [{owner['role']}]")
