import os, json, hashlib, time

def get_file_hash(filepath):
    sha512 = hashlib.sha512()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha512.update(chunk)
        return sha512.hexdigest()
    except Exception:
        return None

def build_omni_merkle_tree():
    print("[+] Scanning workspace for recursive Merkle DAG root calculation...")
    file_hashes = {}
    
    for root, dirs, files in os.walk("."):
        if ".git" in root or "manifests" in root:
            continue
        for file in files:
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, ".")
            h = get_file_hash(path)
            if h:
                file_hashes[rel_path] = h

    sorted_files = sorted(file_hashes.keys())
    master_hasher = hashlib.sha512()
    for f in sorted_files:
        master_hasher.update(f.encode("utf-8"))
        master_hasher.update(file_hashes[f].encode("utf-8"))
        
    master_root = master_hasher.hexdigest()
    
    payload = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "scope": "OMNI_WORKSPACE_RECURSIVE_MERKLE",
        "total_files_hashed": len(sorted_files),
        "master_merkle_root": master_root,
        "file_manifest": file_hashes
    }
    
    os.makedirs("manifests", exist_ok=True)
    manifest_path = "manifests/omni_workspace_merkle_root.json"
    with open(manifest_path, "w") as f:
        json.dump(payload, f, indent=2)
        
    print(f"    -> Hashed {len(sorted_files)} workspace files.")
    print(f"    -> Master Merkle Root: {master_root[:32]}... [SHA-512 SECURED]")
    return master_root

if __name__ == "__main__":
    root = build_omni_merkle_tree()
    os.system("git add .")
    os.system(f'git commit -m "OMNI-MERKLE // Root: {root[:12]}... [All Workspace Files Sealed]"')
    branch_name = f"omni-merkle-{time.strftime('%Y%m%d-%H%M%S')}"
    os.system(f"git checkout -b {branch_name}")
    os.system(f"git push -u origin {branch_name} --force")
    print("[+] Omni-Workspace Merkle Tree Push Complete, bruz!")
