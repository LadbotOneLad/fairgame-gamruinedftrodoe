// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AtomTruthStateProofs is ERC721URIStorage, Ownable {
    
    struct StateProof {
        string genesisHash;
        bytes32 merkleRoot;
        bytes20 gitCommit;
        uint256 timestamp;
    }

    mapping(uint256 => StateProof) public registry;

    constructor() ERC721("AtomTruthRootAuthority", "ATRA") Ownable(msg.sender) {}

    function sealStateProof(
        address to,
        uint256 tokenId,
        string memory genesis,
        bytes32 merkle,
        bytes20 commit,
        string memory tokenURI
    ) external onlyOwner {
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        registry[tokenId] = StateProof({
            genesisHash: genesis,
            merkleRoot: merkle,
            gitCommit: commit,
            timestamp: block.timestamp
        });
    }
}
