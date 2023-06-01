// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.2/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.3.2/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract AuthentiChainMinting is ERC721URIStorage {
    // A mapping to keep track of token's ownership history.
    mapping (uint256 => address[]) private _ownerHistory;

    // A mapping to ensure uniqueness of token URIs.
    mapping (bytes32 => bool) private _usedURIs;

    // Constructor sets the name and symbol of the token.
    constructor() ERC721("AuthentiChain", "ATCH") {}

    // Public function to mint new tokens. 
    // Any address can mint a new token with unique metadata.
    function mint(address to, uint256 tokenId, string memory tokenURI) public {
        bytes32 uriHash = keccak256(abi.encodePacked(tokenURI));
        require(!_usedURIs[uriHash], "Token URI has already been used");
        
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _ownerHistory[tokenId].push(to);
        
        _usedURIs[uriHash] = true;
    }

    // Function to get the ownership history of a token.
    function ownerHistory(uint256 tokenId) public view returns (address[] memory) {
        return _ownerHistory[tokenId];
    }

    // Overriding the _beforeTokenTransfer function to include a step that keeps track of the token's ownership history.
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
        if (to != address(0)) {
            _ownerHistory[tokenId].push(to);
        }
    }
}