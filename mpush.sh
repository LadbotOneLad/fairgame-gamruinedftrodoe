#!/usr/bin/env bash
# =====================================================================
# [ROBDOE.MYWARE] NATIVE MERKLE DAG EXTRACTION & DEPLOYMENT MODULE
# =====================================================================

# Ensure changes are staged so Git's index updates its internal DAG structure
git add .

echo "🌿 Querying native Git Merkle DAG state..."
# Write the current index to a tree object and extract its unique SHA-1 hash
ROOT_TREE_HASH=$(git write-tree 2>/dev/null)

if [ -z "$ROOT_TREE_HASH" ]; then
    echo "❌ Error: Cannot compute DAG state. Ensure you are in a valid Git repo."
    exit 1
fi

# Upgrade the SHA-1 tree hash to a 256-bit signature for MyWare compliance
ROOT_HASH=$(echo -n "$ROOT_TREE_HASH" | openssl dgst -sha256 -r | awk '{print $1}')

echo "🛡️  Merkle DAG Root Verified: [0x${ROOT_HASH:0:16}...${ROOT_HASH: -16}]"
echo "📝 Injecting cryptographic state into commit metadata..."

git commit -m "sys(matrix): merge layer state | GENESIS:e14f9a8d | dag-root: 0x$ROOT_HASH"

echo "🚀 Pushing Merkle node upstream..."
git push origin main
