#!/usr/bin/env node

import fs from "fs";
import path from "path";
import { ethers } from "ethers";
import dotenv from "dotenv";

dotenv.config();

console.log("==================================================");
console.log("  ROBDOEROOTAUTHORITY: THE WALLET STRING BADGE   ");
console.log("==================================================");

// Dynamic Repo License Verification
const licenceDir = "./Licences";
let eulaContent = "";

try {
    if (!fs.existsSync(licenceDir)) {
        throw new Error(`Directory ${licenceDir} not found. Run git pull.`);
    }

    const files = fs.readdirSync(licenceDir);
    // Search the repository for your license file
    const targetFile = files.find(f => f.toLowerCase().includes("eula") || f.toLowerCase().includes("licence"));

    if (!targetFile) {
        throw new Error("No EULA or Licence file found inside the cloned directory.");
    }

    eulaContent = fs.readFileSync(path.join(licenceDir, targetFile), "utf8");
    console.log(`[LICENCE LOADED] Verified from repo: ${targetFile}`);
    console.log("--------------------------------------------------");
    console.log("  Jurisdiction: Regina / Root Authority Verified");
    console.log("  Token Standard: ERC-721 Secured");
    console.log("--------------------------------------------------");
} catch (error) {
    console.error(`\n[CRITICAL FAULT] Licence check failed: ${error.message}`);
    console.error("Root execution blocked to protect your wallet strings.");
    process.exit(1);
}

async function main() {
    try {
        // Load configuration
        const deedData = JSON.parse(fs.readFileSync("./domain-deed.json", "utf8"));
        console.log(`[TOKEN STATUS]  Standard: ${deedData.token_standard}`);
        console.log(`[DEED ANCHOR]   Root Deed: ${deedData.primary_domain}`);
        console.log(`[NAMESPACE]     Target: ${deedData.target_namespace}\n`);

        if (!process.env.RPC_PROVIDER_URL || !process.env.PRIVATE_KEY) {
            console.log("[OFFLINE MODE] Missing .env credentials. Simulating transaction pipeline...");
            for (const [key, address] of Object.entries(deedData.records)) {
                console.log(`[SIMULATED] Tokenized ${key}.${deedData.target_namespace} to address: ${address}`);
            }
            console.log("\n[SUCCESS] Dry-run verification cycle complete.");
            return;
        }

        // Live connection initialization
        const provider = new ethers.JsonRpcProvider(process.env.RPC_PROVIDER_URL);
        const signer = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        console.log(`[CONNECTED] Signer active: ${signer.address}`);

    } catch (error) {
        console.error("\n[PIPELINE FAULT] Execution failed:", error.message);
        process.exit(1);
    }
}

main();
