# CLOUDFLARE INFRASTRUCTURE COMPLIANCE & PRIVACY CLAUSE

### 1. EDGE PROXY ROUTING
All remote administrative commands, API webhooks, and state queries sent to or from the System terminal are proxied through the Cloudflare Edge Network. Network traffic is optimized, cached, and inspected for malicious exploitation patterns (DDOS protection, Web Application Firewall).

### 2. NETWORK ACCEPTABLE USE POLICY (AUP)
In compliance with the Cloudflare Self-Serve Subscription Agreement, the User and Operator agree that:
* No high-bandwidth automated scraping loops may target the command endpoint.
* The API connection framework shall not be used to distribute obfuscated payloads or unauthorized bypass scripts.
* Any traffic flagged by Cloudflare’s automated threat intelligence as originating from a compromised IP space or unverified VPN node will be instantly challenged (Turnstile/CAPTCHA) or blacklisted at the network edge before reaching the Termux server environment.

### 3. DATA RETENTION & ENCRYPTION
In-transit packet payloads are encrypted using TLS 1.3 certificates managed via Cloudflare. Local network identifiers (such as local IP assignments routed via mobile gateways) are scrubbed or masked at the edge to protect edge routing confidentiality.
