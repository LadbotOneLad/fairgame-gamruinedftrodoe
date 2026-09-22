// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

interface IERC721 {
    function balanceOf(address owner) external view returns (uint256);
}

contract SovereignDomainHookV4 {
    address public immutable domainRegistry;
    address public immutable poolManager;

    error UnauthorizedDomainHolder();
    error OnlyPoolManager();

    modifier onlyPoolManager() {
        if (msg.sender != poolManager) revertOnlyPoolManager();
        _;
    }

    constructor(address _poolManager, address _domainRegistry) {
        poolManager = _poolManager;
        domainRegistry = _domainRegistry;
    }

    function beforeModifyPosition(
        address sender,
        bytes calldata
    ) external view onlyPoolManager returns (bytes4) {
        if (IERC721(domainRegistry).balanceOf(sender) == 0) {
            revert UnauthorizedDomainHolder();
        }
        return this.beforeModifyPosition.selector;
    }

    function revertOnlyPoolManager() internal pure {
        revert OnlyPoolManager();
    }
}
