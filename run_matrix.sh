#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
TIMESTAMP=$(date "[%Y-%m-%d %H:%M:%S]")

echo "$TIMESTAMP [CRON] Triggering autonomous system sweep..." >> ~/robdoerootauthority/logs/system.log

# Execute MetaMask Matrix Track (Routes logs safely)
if [ -f ~/robdoerootauthority/metamask_wallet/check_metamask.js ]; then
    node ~/robdoerootauthority/metamask_wallet/check_metamask.js >> ~/robdoerootauthority/logs/wallet_history.log 2>&1
fi

# Execute CoinSpot Matrix Track (Routes logs safely)
if [ -f ~/robdoerootauthority/coinspot_wallet.py ]; then
    python ~/robdoerootauthority/coinspot_wallet.py >> ~/robdoerootauthority/logs/wallet_history.log 2>&1
fi
