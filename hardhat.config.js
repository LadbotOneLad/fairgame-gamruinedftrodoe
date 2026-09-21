/**
 * @type import('hardhat/config').HardhatUserConfig
 * @notice Static Solidity Compiler Profile Configurations for 2035 Horizon Architecture.
 */
module.exports = {
  solidity: {
    version: "0.8.26",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      },
      metadata: {
        bytecodeHash: "none"
      }
    }
  },
  paths: {
    sources: "./",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  }
};
