import fs from 'fs';
import path from 'path';
import solc from 'solc';

function findImports(importPath) {
    try {
        let actualPath;
        if (importPath.startsWith('@openzeppelin/')) {
            actualPath = path.resolve('node_modules', importPath);
        } else {
            actualPath = path.resolve('contracts', importPath);
        }
        return { contents: fs.readFileSync(actualPath, 'utf8') };
    } catch (e) {
        return { error: 'File not found: ' + e.message };
    }
}

const contractSource = fs.readFileSync('contracts/AtomTruthStateProofs.sol', 'utf8');

const input = {
    language: 'Solidity',
    sources: { 'AtomTruthStateProofs.sol': { content: contractSource } },
    settings: { 
        optimizer: { enabled: true, runs: 200 },
        evmVersion: "cancun", // Activates the mcopy memory space mapping
        outputSelection: { '*': { '*': ['abi', 'evm.bytecode'] } } 
    }
};

console.log("[*] Resolving OpenZeppelin lattice tree with Cancun EVM parameters...");

const output = JSON.parse(solc.compile(JSON.stringify(input), { import: findImports }));

let hasErrors = false;
if (output.errors) {
    output.errors.forEach(err => {
        console.log(err.formattedMessage);
        if (err.severity === 'error') hasErrors = true;
    });
}

if (!hasErrors) {
    console.log("[+] Compilation successful!");
    fs.writeFileSync('artifacts.json', JSON.stringify(output, null, 2));
    console.log("[+] EVM Bytecode & ABI written to artifacts.json");
}
