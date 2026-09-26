const fs = require('fs');
const solc = require('solc');

// Read the contract source file directly from your workspace
const contractSource = fs.readFileSync('contracts/AtomTruthStateProofs.sol', 'utf8');

const input = {
    language: 'Solidity',
    sources: { 'AtomTruthStateProofs.sol': { content: contractSource } },
    settings: { outputSelection: { '*': { '*': ['abi', 'evm.bytecode'] } } }
};

console.log("[*] Compiling robdoe.com registry via pure solc-js...");
const output = JSON.parse(solc.compile(JSON.stringify(input)));

if (output.errors) {
    output.errors.forEach(err => console.log(err.formattedMessage));
} else {
    console.log("[+] Compilation successful!");
    fs.writeFileSync('artifacts.json', JSON.stringify(output, null, 2));
    console.log("[+] EVM Bytecode & ABI written to artifacts.json");
}
