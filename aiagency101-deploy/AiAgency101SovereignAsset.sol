// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AiAgency101SovereignAsset is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    mapping(address => bool) public coreOwners;
    mapping(uint256 => string) private _stateManifests;
    mapping(uint256 => string) private _siliconTargets;

    event SovereignAssetMinted(address indexed recipient, uint256 indexed tokenId, string merkleRoot, string siliconTarget);
    event CoreOwnerUpdated(address indexed owner, bool status);

    constructor(address[] memory initialOwners) ERC721("AiAgency101 Sovereign Asset", "AA101") Ownable(msg.sender) {
        for (uint i = 0; i < initialOwners.length; i++) {
            coreOwners[initialOwners[i]] = true;
            emit CoreOwnerUpdated(initialOwners[i], true);
        }
    }

    modifier onlyCoreOwner() {
        require(coreOwners[msg.sender] || msg.sender == owner(), "Caller is not a core consensus owner");
        _;
    }

    function mintSovereignAsset(address recipient, string memory merkleRoot, string memory siliconTarget) public onlyCoreOwner returns (uint256) {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _safeMint(recipient, newItemId);
        _stateManifests[newItemId] = merkleRoot;
        _siliconTargets[newItemId] = siliconTarget;
        emit SovereignAssetMinted(recipient, newItemId, merkleRoot, siliconTarget);
        return newItemId;
    }
}
