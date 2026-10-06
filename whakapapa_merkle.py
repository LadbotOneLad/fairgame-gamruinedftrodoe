import hashlib
import json

class WhakapapaNode:
    def __init__(self, name: str, parent_hashes: list[str] = None):
        self.name = name
        self.parent_hashes = parent_hashes or []
        self.node_hash = self._compute_hash()

    def _compute_hash(self) -> str:
        payload = f"{self.name}|{'|'.join(sorted(self.parent_hashes))}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def build_whakapapa_tree():
    print("--- MOLDING MERKLE WHAKAPAPA IWI TREE ---")
    
    # Root Genesis Anchor
    root_genesis = WhakapapaNode("Genesis: e14f9a8d // RobDoe Root Authority")
    
    # Primary Lineage Layers (Tātai)
    atua_layer = WhakapapaNode("HONC Macromolecular Core", [root_genesis.node_hash])
    iwi_layer = WhakapapaNode("RobDoe Pty Ltd / AiAgency101 Mesh", [atua_layer.node_hash])
    hapu_layer = WhakapapaNode("Kinetic Swarm & ESP32 Node Lattice", [iwi_layer.node_hash])
    whanau_node = WhakapapaNode("Active Edge Terminal (Operational Node)", [hapu_layer.node_hash])

    print(f"Root Genesis Hash : {root_genesis.node_hash[:16]}...")
    print(f"Atua Layer Hash   : {atua_layer.node_hash[:16]}...")
    print(f"Iwi Layer Hash    : {iwi_layer.node_hash[:16]}...")
    print(f"Hapū Layer Hash   : {hapu_layer.node_hash[:16]}...")
    print(f"Whānau Terminal   : {whanau_node.node_hash[:16]}...")
    print("\nSTATUS: WHAKAPAPA CRYPTOGRAPHICALLY BOUND TO MANA ROOT.")

if __name__ == "__main__":
    build_whakapapa_tree()
