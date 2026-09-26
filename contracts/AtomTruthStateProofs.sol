// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RobDoeDomainRegistry is ERC721URIStorage, Ownable {
    
    struct DomainRecords {
        string domainName;     // Hardcoded to "robdoe.com"
        bytes32 merkleRoot;    // 0x90869772...
        bytes20 latestCommit;  // 0x09f2ebce...
        uint256 registeredAt;
    }

    mapping(uint256 => DomainRecords) public registry;
    string public constant TARGET_DOMAIN = "robdoe.com";

    constructor() ERC721("RobDoeRootDomain", "RDTI") Ownable(msg.sender) {}

    /**
     * @notice Seals the robdoe.com domain node into the local Merkle matrix history.
     * @param to The wallet address claiming root control of the domain.
     * @param merkle The active tracking matrix root from your jsonl file.
     * @param commit The current Git SHA-1 identifier (0x09f2ebce...).
     */
    function sealRootDomain(
        address to,
        bytes32 merkle,
        bytes20 commit
    ) external onlyOwner {
        uint256 tokenId = uint256(keccak256(abi.encodePacked(TARGET_DOMAIN)));
        
        _safeMint(to, tokenId);

        registry[tokenId] = DomainRecords({
            domainName: TARGET_DOMAIN,
            merkleRoot: merkle,
            latestCommit: commit,
            registeredAt: block.timestamp
        });
    }
}
