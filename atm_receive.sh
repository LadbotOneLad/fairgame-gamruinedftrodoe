#!/usr/bin/env bash

PORT=9000
echo "🚀 [GENESIS ONLINE] Monitoring Vodafone Hotspot Port $PORT..."

# Keep an infinite socket listener alive to receive deposit packets
while true; do
    # Listen on port 9000 and capture the transaction message
    PACKET=$(nc -l -p $PORT)
    
    if [[ "$PACKET" == *"CREDITS_DEPOSITED"* ]]; then
        # Parse the credit count safely
        CREDITS=$(echo "$PACKET" | cut -d':' -f2)
        echo "💰 [VALIDATED] Deposit Received! Value: $CREDITS credit(s) sent to core system."
        
        # --- EXECUTE YOUR ARCADES / GAME HOOKS HERE ---
    fi
done
