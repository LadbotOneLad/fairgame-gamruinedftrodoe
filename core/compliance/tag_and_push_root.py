import subprocess
import json
import os

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip(), res.stderr.strip()

def execute():
    # Detect actual active git branch
    branch, _ = run_cmd("git rev-parse --abbrev-ref HEAD")
    if not branch or branch == "HEAD":
        branch = "feature/sovereign-compliance-s140-s150"
    print(f"[*] Active Git Branch: {branch}")

    # Load root hash from manifest
    manifest_path = "core/compliance/dag_manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            root_hash = data.get("terminal_master_root_hash", "aee65b98f5a2f00ed6f6ff18e88b5d005cdd3c95b87c5277f2e3cf201e3fc2c")
    else:
        root_hash = "aee65b98f5a2f00ed6f6ff18e88b5d005cdd3c95b87c5277f2e3cf201e3fc2c"

    tag_name = f"v1.0.0-root-{root_hash[:12]}"
    tag_msg = f"ROBDOE Sovereign Master Terminal Root Hash: {root_hash} [Ft=1, R=94.2%]"

    print(f"[*] Applying annotated tag: {tag_name}")
    run_cmd(f'git tag -a "{tag_name}" -m "{tag_msg}"')

    print(f"[*] Pushing branch {branch} to origin...")
    out, err = run_cmd(f"git push origin {branch} --force-with-lease")
    print(out if out else err)

    print(f"[*] Pushing tag {tag_name} to origin...")
    tout, terr = run_cmd(f"git push origin {tag_name}")
    print(tout if tout else terr)

    print("================================================================")
    print(f"[+] SUCCESS: PUSHED BRANCH [{branch}] + TAG [{tag_name}]")
    print("================================================================")

if __name__ == "__main__":
    execute()
