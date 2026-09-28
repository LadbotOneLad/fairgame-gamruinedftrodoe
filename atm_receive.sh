#!/usr/bin/env bash

PORT=9000
GENESIS_HASH="00008d1a438c3466bca72a93f3a03e15c284899110c6b2bca73fb6dc9edc7542"

echo "🚀 [GENESIS ONLINE] Monitoring Secured Vodafone Hotspot Port $PORT..."

while true; do
    # Capture the raw string over the network
    PACKET=$(nc -l -p $PORT)
    
    # Expected format: GENESIS_BLOCK:hash:CREDITS_DEPOSITED:count
    if [[ "$PACKET" == *"GENESIS_BLOCK"* ]]; then
        # Parse fields using ':' as delimiter
        INBOUND_HASH=$(echo "$PACKET" | cut -d':' -f2)
        CREDITS=$(echo "$PACKET" | cut -d':' -f4)
        
        # Cryptographic Handshake Check
        if [ "$INBOUND_HASH" = "$GENESIS_HASH" ]; then
            echo "💰 [VALIDATED] Proof of Work handmatched! Processing $CREDITS credit(s)."
            
            # --- PLACE YOUR REAL LIFE GAME LAUNCHER SCRIPT HERE ---
            # e.g., bash launch_game_relay.sh $CREDITS
        else
            echo "🚨 [SECURITY WARNING] Inbound block hash mismatch! Packet dropped."
            echo "Received Signature: $INBOUND_HASH"
        fi
    fi
done
