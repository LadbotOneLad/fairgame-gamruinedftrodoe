#!/usr/bin/env bash
# =====================================================================
# [ROBDOE.MYWARE] PURE MATHEMATICAL MERKLE TREE COMPUTATION ENGINE
# =====================================================================

echo "🌿 Step 1: Generating Leaf Nodes (H(Data)) from raw file binaries..."

# Find all tracked files, strip tracking folders (.git), and sort deterministically
FILES=$(find . -type f ! -path '*/.*' ! -name 'pure_math_merkle.sh' | sort)

# Calculate SHA-256 hashes of every file's raw contents
LEAF_HASHES=$(echo "$FILES" | while read -r file; do
    if [ -f "$file" ]; then
        # Extract purely the hex hash string from the file stream
        openssl dgst -sha256 -binary "$file" | xxd -p | tr -d '\n'
        echo ""
    fi
done | sed '/^$/d')

NODE_COUNT=$(echo "$LEAF_HASHES" | wc -l)
echo "🧬 Hashed $NODE_COUNT raw filesystem leaves."

# Define the tree reduction function
CURRENT_LAYER="$LEAF_HASHES"
LAYER_NUM=0

while [ $(echo "$CURRENT_LAYER" | wc -l) -gt 1 ]; do
    LAYER_NUM=$((LAYER_NUM + 1))
    NEXT_LAYER=""
    LEFT_NODE=""
    
    while read -r current_hash; do
        if [ -z "$LEFT_NODE" ]; then
            LEFT_NODE="$current_hash"
        else
            # Mathematical concatenation and hashing: H(Left + Right)
            PARENT_HASH=$(echo -n "${LEFT_NODE}${current_hash}" | xxd -r -p | openssl dgst -sha256 -binary | xxd -p | tr -d '\n')
            NEXT_LAYER="${NEXT_LAYER}${PARENT_HASH}"$'\n'
            LEFT_NODE=""
        fi
    done <<< "$CURRENT_LAYER"
    
    # If a layer has an odd number of nodes, duplicate the un-paired node: H(Left + Left)
    if [ -n "$LEFT_NODE" ]; then
        PARENT_HASH=$(echo -n "${LEFT_NODE}${LEFT_NODE}" | xxd -r -p | openssl dgst -sha256 -binary | xxd -p | tr -d '\n')
        NEXT_LAYER="${NEXT_LAYER}${PARENT_HASH}"$'\n'
    fi
    
    CURRENT_LAYER=$(echo "$NEXT_LAYER" | sed '/^$/d')
    echo "📐 Layer $LAYER_NUM collapsed down to $(echo "$CURRENT_LAYER" | wc -l) nodes."
done

ROOT_HASH=$(echo "$CURRENT_LAYER" | tr -d '\n')
echo "====================================================================="
echo "🛡️  MATHEMATICAL MERKLE ROOT RESOLVED:"
echo "0x$ROOT_HASH"
echo "====================================================================="
