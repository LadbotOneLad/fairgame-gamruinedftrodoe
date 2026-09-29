import { MerkleTree } from 'merkletreejs';
import keccak256 from 'keccak256';

// 1. Raw distributed domain metadata array
const domains = [
  "1.com",
  "robertdoe.pw",
  "aiagency101.xyo",
  "aiagency101.pw"
];

// 2. Compute separate Leaf hashes using Keccak-256 (Ethereum Native)
const leaves = domains.map(domain => keccak256(domain));

// 3. Construct the Merkle Tree hierarchy (sorting pairs to prevent multi-proof exploits)
const tree = new MerkleTree(leaves, keccak256, { sortPairs: true });
const rootHash = tree.getRoot().toString('hex');

console.log("\n\x1b[38;5;226m=========================================================\x1b[0m");
console.log(`\x1b[1;38;5;46m[MERKLE ROOT HASH]:\x1b[0m 0x${rootHash}`);
console.log("\x1b[38;5;226m=========================================================\x1b[0m");

// 4. Extract the exact cryptographic verification proof vector for 1.com
const targetDomain = "1.com";
const targetLeaf = keccak256(targetDomain);
const proof = tree.getHexProof(targetLeaf);

console.log(`\n\x1b[38;5;51m[VERIFICATION PROOF FOR ${targetDomain.toUpperCase()}]:\x1b[0m`);
console.log(JSON.stringify(proof, null, 2));

// 5. Bare-metal verification check inside the runtime environment
const isVerified = tree.verify(proof, targetLeaf, rootHash);
console.log(`\n\x1b[1mStatus Validation:\x1b[0m ${isVerified ? "✅ MATCHED / SECURE" : "❌ INVALID PROOF"}\n`);
