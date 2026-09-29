#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\x1b[38;5;226m=====================================================================\x1b[0m"
echo -e "\x1b[1;38;5;51m[SANITZED MONOLITH LEDGER ENGINE v2.0]\x1b[0m | Target String: \x1b[38;5;82m1.com\x1b[0m"
echo -e "\x1b[38;5;226m=====================================================================\x1b[0m"

# Execute programmatic JS engine directly using strict HTTP streaming
node -e "
import { namehash } from 'viem';

async function fetchOnChainState() {
  const hash = namehash('1.com');
  const tokenId = hash.replace('0x', '').padStart(64, '0');
  const contract = '0x049aba7510f45ba5b64ea9e658e342f904db358d';
  const payload = '0x6352211e' + tokenId;

  console.log('Computed Namehash :', hash);
  console.log('Firing Cryptographic JSON-RPC Stream...');

  try {
    const response = await fetch('https://ankr.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'eth_call',
        params: [{ to: contract, data: payload }, 'latest'],
        id: 1
      })
    });

    const text = await response.text();
    
    // Check if the response is raw HTML (Cloudfront/Cloudflare Block)
    if (text.trim().startsWith('<')) {
      console.log('\n\x1b[38;5;196m[EDGE PROXY BLOCK]:\x1b[0m Node edge returned HTML gateway data instead of a ledger state.');
      return;
    }

    const json = JSON.parse(text);
    if (json.error) {
      console.log('\n\x1b[38;5;196m[RPC EXCEPTION]:\x1b[0m ' + json.error.message);
    } else if (json.result) {
      const cleanAddress = '0x' + json.result.slice(-40);
      console.log('\n\x1b[1;38;5;46m[LIVE ON-CHAIN METADATA OWNER]:\x1b[0m ' + cleanAddress + '\n');
    }
  } catch (err) {
    console.log('\n\x1b[38;5;196m[STREAMING FAULT]:\x1b[0m ' + err.message);
  }
}

fetchOnChainState();
"
