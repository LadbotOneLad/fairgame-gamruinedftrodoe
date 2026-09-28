#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"

# Structural folder initialization
mkdir -p ~/robdoerootauthority/logs
touch ~/robdoerootauthority/logs/matrix_infinite.log

while true; do
    # Run the foreground miquidutit liquidity pipeline directly
    node ~/robdoerootauthority/foreground_matrix.js >> ~/robdoerootauthority/logs/matrix_infinite.log 2>&1
    
    # If the process terminates, log the drop and wait 2 seconds before instant reincarnation
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [SYSTEM_WARNING] Matrix collapsed. Triggering Merkle reboot..." >> ~/robdoerootauthority/logs/matrix_infinite.log
    sleep 2
done
