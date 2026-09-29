import { MerkleTree } from 'merkletreejs';
import keccak256 from 'keccak256';
import { namehash, labelhash } from 'viem';

// 1. Raw distributed domain data
const domains = [
  "1.com",
  "robertdoe.pw",
  "aiagency101.xyo",
  "aiagency101.pw"
];

// 2. Compute the ACTUAL on-chain Namehash for each leaf node
const leaves = domains.map(domain => {
  const hashString = namehash(domain);
  // Convert hex string to raw buffer for the Merkle Tree
  return Buffer.from(hashString.replace('0x', ''), 'hex');
});

// 3. Build the hierarchical Merkle Tree structure
const tree = new MerkleTree(leaves, keccak256, { sortPairs: true });
const rootHash = tree.getRoot().toString('hex');

console.log("\n\x1b[38;5;226m=========================================================\x1b[0m");
console.log(`\x1b[1;38;5;46m[CORRECTED ON-CHAIN MERKLE ROOT]:\x1b[0m 0x${rootHash}`);
console.log("\x1b[38;5;226m=========================================================\x1b[0m");

// 4. Extract the genuine Namehash verification vector for 1.com
const targetDomain = "1.com";
const targetNamehash = Buffer.from(namehash(targetDomain).replace('0x', ''), 'hex');
const proof = tree.getHexProof(targetNamehash);

console.log(`\n\x1b[38;5;51m[GENUINE CONTRACT PROOF FOR ${targetDomain.toUpperCase()}]:\x1b[0m`);
console.log(`Leaf Namehash: ${namehash(targetDomain)}`);
console.log(JSON.stringify(proof, null, 2));

// 5. Verification validation
const isVerified = tree.verify(proof, targetNamehash, rootHash);
console.log(`\n\x1b[1mContract State Validation:\x1b[0m ${isVerified ? "✅ READY FOR LIVE DEPLOYMENT" : "❌ SYSTEM FAULT"}\n`);
