import time
import hmac
import hashlib
import requests
import json

# ==========================================
# 🔑 ENTER YOUR COINSPOT API KEYS BELOW
# ==========================================
API_KEY = "YOUR_API_KEY_HERE"
SECRET_KEY = "YOUR_SECRET_KEY_HERE"
# ==========================================

url = "https://coinspot.com.au"
nonce = int(time.time() * 1000)

payload = {"nonce": nonce}
payload_json = json.dumps(payload, separators=(',', ':'))

signer = hmac.new(SECRET_KEY.encode('utf-8'), payload_json.encode('utf-8'), hashlib.sha512)
signature = signer.hexdigest()

headers = {
    "Content-Type": "application/json",
    "key": API_KEY,
    "sign": signature
}

try:
    response = requests.post(url, data=payload_json, headers=headers)
    data = response.json()
    
    if data.get("status") == "ok":
        balances_list = data.get("balances", [])
        btc_found = False
        for coin_entry in balances_list:
            if "BTC" in coin_entry:
                btc_data = coin_entry["BTC"]
                print("\n₿ --- Bitcoin Wallet Balance ---")
                print(f"BTC Balance : {btc_data.get('balance', 0)}")
                print(f"Value (AUD) : ${btc_data.get('audbalance', 0):,.2f}")
                print(f"Current Rate: ${btc_data.get('rate', 0):,.2f}")
                btc_found = True
                break
        if not btc_found:
            print("\n❌ BTC balance entry not found or account holds 0 BTC.")
    else:
        print("CoinSpot API Error:", data.get("message"))
except Exception as e:
    print("Connection error:", str(e))
