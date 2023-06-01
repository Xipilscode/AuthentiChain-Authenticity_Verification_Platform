# Import necessary libraries
import os
from dotenv import load_dotenv
import streamlit as st
from web3 import Web3
import ipfshttpclient
import qrcode
from PIL import Image
import requests
import json
from web3.middleware import geth_poa_middleware
from pathlib import Path

# Setting the title for the app
st.set_page_config(page_title='AuthentiChain')

# Setup the main structure of the app using radio buttons for navigation
pages = ["Home", "Creator's Lab", "Distributor's Desk", "Buyer's Archive", "Gas Fees Forecast"]
page = st.sidebar.radio('Navigation', pages)

# Conditional statements to control the flow of the app
if page == 'Home':

    # # Adding a gif from the GitHub repository
    # st.image(
    # "https://github.com/yourgithubusername/yourrepositoryname/raw/main/path_to_your_gif.gif",
    # use_column_width=True
    # )
    
    st.markdown(
    """
    <h2 style="text-align: center;">
    AuthentiChain: 
    <br/>
    Authenticity Verification Platform
    <br/>
    <br/>
    """,
    unsafe_allow_html=True,
    )

    # Providing a description for AuthentiChain
    st.header("About AuthentiChain")
    st.write("""
    AuthentiChain is a platform that leverages the power of blockchain technology to ensure the authenticity of goods and digital content. Whether you are a creator, a distributor, or a buyer, AuthentiChain provides a trustworthy system to verify authenticity and ownership.

    Here's how AuthentiChain works:

    1. **Creator's Lab**: As a creator, you can input data about your product or content. You can then mint a new Non-Fungible Token (NFT) on the blockchain, which represents your product or content uniquely.

    2. **Distributor's Desk**: As a distributor, you can view all the NFT tokens transferred to you from the creator. When you make a sale, you can transfer the ownership of the NFT to the buyer. This information is recorded on the blockchain as a part of the NFT's ownership history.

    3. **Buyer's Archive**: As a buyer, you can view and manage your acquired assets. Each token represents a product or content you've purchased. If you choose to sell your product or content to someone else, you can transfer the ownership of the token. This action updates the chain of ownership, which can be traced back through the history stored on the blockchain.

    4. **Gas Fees Forecast**: Transactions on the blockchain involve certain fees, commonly referred to as 'gas fees'. In order to help users manage these costs, we've integrated a forecasting tool that leverages Machine Learning models such as ARIMA and Prophet to predict future gas fee trends. 

    Welcome to AuthentiChain, a new era of transparent, verifiable, and immutable authenticity verification.
    """)

    st.header("To Get Started")
    st.write("Choose a section from the sidebar to begin using AuthentiChain.")
    
elif page == "Creator's Lab":
    st.title("Creator's Lab")
    # Load environment variables
    load_dotenv()

    # Connect to Ganache
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Necessary for Ganache
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Check if connected
    if not web3.isConnected():
        st.write("Not connected to Ganache. Please check your Ganache instance.")
    else:
        st.write("Successfully connected to Ganache.")

    # Get the first account from Ganache
    account = web3.eth.accounts[0]

    # # Load the contract ABI
    # abi_file_path = Path("./AuthentiChain/AuthentiChainMinting_abi.json")
    
    # with abi_file_path.open(mode="r") as file:
    #     AUTHENTICHAINMINTING_CONTRACT_ABI = json.load(file)


    # # Get the contract address from .env
    # AUTHENTICHAINMINTING_CONTRACT_ADDRESS = os.getenv("AUTHENTICHAINMINTING_CONTRACT_ADDRESS")

    # # Setup the contract
    # contract = web3.eth.contract(address=AUTHENTICHAINMINTING_CONTRACT_ADDRESS, abi=AUTHENTICHAINMINTING_CONTRACT_ABI)

    # Data collection fields
    st.header("Enter your product details:")
    creator_name = st.text_input("Creator's Name")
    product_name = st.text_input("Product Name")
    description = st.text_input("Description")
    creation_date = st.date_input("Creation Date")

    # Mint the NFT
    if st.button('Mint NFT'):

        # Prepare the metadata
        metadata = {
            "name": product_name,
            "description": description,
            "image": "",  # You would normally link to an image file here
            "attributes": {
                "creator": creator_name,
                "creation_date": creation_date.strftime("%Y-%m-%d")
            }
        }

        # Save the metadata to IPFS using Pinata
        pinata_api_key = os.getenv("PINATA_API_KEY")
        pinata_secret_api_key = os.getenv("PINATA_SECRET_API_KEY")
        headers = {
            "pinata_api_key": pinata_api_key,
            "pinata_secret_api_key": pinata_secret_api_key
        }
        response = requests.post("https://api.pinata.cloud/pinning/pinJSONToIPFS", json=metadata, headers=headers)
        ipfs_hash = response.json()["IpfsHash"]

        # Generate a QR code for the IPFS hash
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(ipfs_hash)
        qr.make(fit=True)
        img_qr = qr.make_image(fill="black", back_color="white")
        img_qr.save("qrcode.png")

        # Display the QR code
        st.image(Image.open("qrcode.png"), caption="IPFS QR Code")

        # Call the mint function from the contract
        txn = contract.functions.mint("ipfs://"+ipfs_hash).buildTransaction({
            'from': account,
            'nonce': web3.eth.getTransactionCount(account)
        })
        signed_txn = web3.eth.account.signTransaction(txn, private_key=os.getenv("PRIVATE_KEY"))

        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        # If successful, display the transaction hash
        if receipt is not None:
            st.success("Minting successful! Transaction hash: {}".format(receipt['transactionHash'].hex()))
        else:
            st.error("Minting failed.")









    # Wallet Connection
    st.subheader('Wallet Connection')
    private_key = st.text_input('Private Key', type="password")

    if private_key:
        account = web3.eth.account.privateKeyToAccount(private_key)
        st.write(f'Wallet Address: {account.address}')
    else:
        st.write("Please enter your private key.")








elif page == "Distributor's Desk":
    st.title("Distributor's Desk")
    # We'll implement this section in the next steps

    # Page description
    st.write("""
    As a distributor, you can view all the NFT tokens transferred to you from the creator. When you make a sale, you can transfer the ownership of the NFT to the buyer. This information is recorded on the blockchain as part of the NFT's ownership history.
    """)



    # Retrieve the NFT tokens transferred to the distributor
    distributor_address = "0x..."  # Replace with the distributor's Ethereum address
    nft_tokens = []  # Placeholder for the list of NFT tokens

    # Create a data frame for the transferred NFTs
    nft_data = {
        "Token ID": nft_tokens,
        "Buyer's Ethereum Address": [None] * len(nft_tokens),
        "Transfer Ownership": [False] * len(nft_tokens)
    }
    df = pd.DataFrame.from_dict(nft_data)

    # Display the data frame
    if not df.empty:
        st.subheader("NFT Tokens:")
        st.dataframe(df)

        # Update the data frame with user inputs
        for index, row in df.iterrows():
            buyer_address = st.text_input(f"Buyer's Ethereum Address for Token {row['Token ID']}")
            transfer_button = st.button(f"Transfer Ownership of Token {row['Token ID']}")

            if transfer_button:
                # Perform the transfer of ownership
                # Replace the code below with the actual transfer function from the contract
                transaction_hash = "..."  # Placeholder for the transaction hash
                df.at[index, "Buyer's Ethereum Address"] = buyer_address
                df.at[index, "Transfer Ownership"] = True
                st.write(f"Ownership of Token {row['Token ID']} transferred. Transaction Hash: {transaction_hash}")

        # Display the updated data frame
        st.subheader("Updated NFT Tokens:")
        st.dataframe(df)
    else:
        st.write("No NFT tokens transferred to the distributor.")












elif page == "Buyer's Archive":
    st.title("Buyer's Archive")
    # We'll implement this section in the next steps
