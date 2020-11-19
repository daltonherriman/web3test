from web3 import Web3

infura_url = ""
wallet = ""

# Make web3 connection
web3 = Web3(Web3.HTTPProvider(infura_url))
#print if we're connected to infura
is_connected = web3.isConnected()
print(f'Connected  to Infura -> {is_connected}')

# Get latest ethereum block
block_number = web3.eth.blockNumber
print(f'Current Block Number -> {block_number}')

# Get wallet balance
account_balance = web3.eth.getBalance(wallet)
print(f'Connected to account -> {wallet}')
account_balance = web3.fromWei(account_balance, 'ether')
print(f'Wallet Balance -> {account_balance} ETH.')

