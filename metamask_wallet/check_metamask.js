import http from 'https';

const WALLET = "0x84CA4aFC3F395ebc0b519680B546Cd604C9c2018";
const url = `https://ethplorer.io{WALLET}?apiKey=freekey`;

console.log(`\n🔍 Mass-scanning portfolio for: ${WALLET}`);
console.log(`📦 Analyzing your 80 imported assets... Please wait...\n`);

http.get(url, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        try {
            const json = JSON.parse(data);
            
            // 1. Get Main ETH Balance
            const ethBalance = json.ETH ? json.ETH.balance : 0;
            console.log("=========================================");
            console.log(`🦊 MAIN BALANCE: ${ethBalance.toFixed(6)} ETH`);
            console.log("=========================================");

            // 2. Loop through all 80+ Custom Tokens
            if (json.tokens && json.tokens.length > 0) {
                console.log(`\n🪙 --- Found Assets (${json.tokens.length} Active Tokens) ---`);
                json.tokens.forEach(t => {
                    const tokenName = t.tokenInfo.name || "Unknown Token";
                    const symbol = t.tokenInfo.symbol || "???";
                    const decimals = parseInt(t.tokenInfo.decimals || 18);
                    const rawBalance = t.balance;
                    
                    // Format mass decimals
                    const formattedBalance = rawBalance / Math.pow(10, decimals);
                    
                    if (formattedBalance > 0) {
                        console.log(`🔹 ${symbol} (${tokenName}): ${formattedBalance.toLocaleString(undefined, {maximumFractionDigits: 6})}`);
                    }
                });
            } else {
                console.log("\n⚠️ No on-chain token balances detected on Ethereum Mainnet.");
                console.log("💡 Tip: If your 80 tokens are on Base, Polygon, or Arbitrum networks, we just need to swap the API endpoint string!");
            }
            console.log("\n=========================================");
        } catch (e) {
            console.log("❌ Failed to parse portfolio data mapping.");
        }
    });
}).on('error', (err) => {
    console.log("❌ Network interface timed out: " + err.message);
});
