# Imports 
import json
from web3 import Web3 

infura_url = ''
wallet = ''

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(infura_url))

# Save the connection state
is_connected = web3.isConnected()

abi = ''
address = ''