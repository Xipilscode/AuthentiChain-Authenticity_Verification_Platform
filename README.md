# AuthentiChain: Authenticity Verification Platform

AuthentiChain is an innovative solution aimed at addressing counterfeiting issues across various industries, including luxury goods, wine, and medicine. By leveraging the capabilities of Ethereum's blockchain technology, smart contracts written in Solidity, and an intuitive user interface designed using Streamlit, AuthentiChain offers a secure, transparent, and user-friendly platform for manufacturers, supply chain partners, and consumers.

### Technology Stack
The technologies utilized in this project include:

* Blockchain platform: Ethereum - The core platform for deploying our smart contracts and creating the underlying blockchain network.
* Smart contract language: Solidity - The primary language used for writing the logic and rules of our blockchain-based operations.
* User interface: Streamlit - Used for building an intuitive and user-friendly front-end for easy interaction with the application.
* Machine learning model: ARIMA, Prophet, Integrated i.i.d. Noise model - Leveraged these models to predict the Ethereum network's gas fees, thereby helping users make informed transaction decisions.
* Local Blockchain: Ganache - Used for local blockchain development and testing. It offers a personal Ethereum blockchain, which is beneficial for examining and debugging before deployment to the mainnet or testnet.
* Smart Contract IDE: Remix IDE - An online IDE that aids in writing, testing, debugging, and deploying Solidity smart contracts.
* Blockchain Wallet: Metamask - Used as the Ethereum wallet, providing a secure identity vault and a user-friendly bridge that allows users to run Ethereum dApps right in their browser without running a full Ethereum node.

### Conclusion and Future Directions
AuthentiChain is an easy-to-adopt solution utilizing Ethereum, Solidity, and Streamlit. With its decentralized authenticity verification system, the platform can revolutionize various sectors by ensuring product and content integrity.

Future directions include the implementation of a sustainable business model with various strategies like Subscription, Pay-Per-Use, and Premium Models, alongside optimizations for gas fees, in-app ads, and additional data and analytics services.

### Overview
This repository contains the code for our decentralized application, which leverages the power of blockchain and NFTs to ensure the authenticity and traceability of goods and digital content. Our solution is built around three main modules:

* Creator's Lab
* Distributor's Desk
* Buyer's Archive
Additionally, we have developed smart contracts which allow us to interact with the blockchain in a secure and reliable way. This description will guide you through the functionalities of each module and smart contract.

#### Creator's Lab
Creators, either manufacturers of physical goods or digital content creators, use this interface to input vital information about their product or content. This metadata is used to create a unique NFT token representing the product or content on the blockchain. Additionally, a QR code is generated, storing the metadata on IPFS, a decentralized storage platform. Upon creation of the metadata and QR code, the creator can mint the NFT token on the blockchain, beginning the chain of ownership.

#### Distributor's Desk
Retailers, galleries, online platforms, and other distributors use this interface to manage the NFT tokens transferred to them by the creators. They can view a list of all their tokens and transfer ownership to a customer upon sale. This information is recorded in the blockchain, maintaining the chain of ownership. This is a crucial aspect in verifying the authenticity of a product or digital content.

#### Buyer's Archive
End users or buyers can view and manage their acquired assets here. Every owned token, representing a purchased product or content, can be seen in this section. Users can also verify the product or content by scanning the associated QR code to access information stored on IPFS. Moreover, they can transfer the ownership of the token if they decide to sell the product or content, hence updating the chain of ownership.

#### Smart Contracts
##### AuthentiChainContract

This ERC721 contract serves as the foundation for our application. Besides providing the standard ERC721 functionality, it includes additional features for minting, metadata management, and ownership tracking.

* Minter Role: This role is assigned by the contract owner to trusted manufacturers, allowing them to mint new tokens.

* Metadata Management: When a new token is minted, the associated IPFS hash, which is linked to the product's metadata, is recorded.

* Ownership Management: The contract tracks the history of token ownership, storing this information in the blockchain.

* TokenURI Implementation: This function provides a URI linking to the product's metadata stored on IPFS.

##### AuthentiChainManagement Contract

This contract, similar to AuthentiChainContract, includes basic ERC721 functionality and additional features for minting, metadata handling, and ownership tracking.

* Minter Role: In this contract, any address can mint a token.

* Metadata Management: Each minted token is linked to a unique URI, typically an IPFS hash of the product's metadata.

* Ownership Management: Similar to the AuthentiChainContract, it records the history of owners for each token.

* TokenURI Implementation: It returns a URI linked to the token's metadata.

Our implementation combines blockchain, IPFS, and QR codes to create a robust, user-friendly system for verifying the authenticity and ownership of both physical and digital assets. This transparent chain of ownership prevents counterfeiting and unauthorized duplication, thus ensuring trust and reliability in the system.

### Time series models training approach:
Leverage on year of historical Ethereum gas prices sampled as daily last values Split historical data into training and test datasets using 80/20. Conduct an initial data exploration to discover general trends and fluctuations. Fit a model using Prophet using default and tuned hyperparameters. Make a future dataset for the prediction forecasts based on a 7-day rolling window. Analyze the predictions on the test data and calculate performance metrics. Compare the forecasted values to the actual values in the simulated forecast for the time horizon.