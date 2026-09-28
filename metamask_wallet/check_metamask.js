// =====================================================================
// [ROBDOE.MYWARE] WEB3 METAMASK RPC HANDSHAKE ENGINE
// =====================================================================
const https = require('https');

const rpcPayload = JSON.stringify({
    jsonrpc: "2.0",
    method: "eth_blockNumber",
    params: [],
    id: 1
});

const options = {
    hostname: 'cloudflare-eth.com',
    port: 443,
    path: '/v1/mainnet',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': rpcPayload.length
    }
};

console.log("⚡ [WEB3-HANDSHAKE] Initialising direct RPC handshake query...");

const req = https.request(options, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        try {
            const parsed = JSON.parse(data);
            console.log(`🛡️  Current Mainnet Block Height: ${parseInt(parsed.result, 16)}`);
        } catch (e) {
            console.log("⚠️  Fallback: Node response encrypted or offline.");
        }
    });
});

req.on('error', (error) => { console.error(`❌ Connection Fault: ${error.message}`); });
req.write(rpcPayload);
req.end();
