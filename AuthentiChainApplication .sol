// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.2/contracts/access/AccessControl.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.2/contracts/token/ERC721/ERC721.sol";

contract AuthentiChainApplication is ERC721, AccessControl {
    // Define a role for the application admin
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    // Mapping to keep track of token's ownership history
    mapping (uint256 => address[]) private _ownerHistory;

    constructor() ERC721("AuthentiChainApplication", "ATCHAPP") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ADMIN_ROLE, msg.sender);
    }

    function getOwnerHistory(uint256 tokenId) public view returns (address[] memory) {
        return _ownerHistory[tokenId];
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
        // If the token is not being burnt
        if(to != address(0)) {
            _ownerHistory[tokenId].push(to);
        }
    }
    
    // The function "supportsInterface" is overridden to resolve the conflict between ERC721 and AccessControl 
    function supportsInterface(bytes4 interfaceId) public view override(ERC721, AccessControl) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}