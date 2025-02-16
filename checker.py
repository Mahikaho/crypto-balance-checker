import os
from web3 import Web3

# BSC public node URL
BSC_NODE_URL = "https://bsc.publicnode.com"  # Public BSC node

# Connect to the BSC node
w3 = Web3(Web3.HTTPProvider(BSC_NODE_URL))

# Ensure the connection to the node is successful
if not w3.is_connected():
    print("Failed to connect to BSC node")
    exit()

def check_wallet_balance(wallet_address):
    try:
        # Get the balance of the wallet (in Wei)
        balance_wei = w3.eth.get_balance(wallet_address)
        
        # Convert the balance from Wei to BNB (Ether in this case)
        balance_bnb = w3.fromWei(balance_wei, 'ether')  # Correct usage
        
        # Print the wallet address and balance
        print(f"Wallet: {wallet_address} has {balance_bnb} BNB")
        return wallet_address, balance_bnb
    except Exception as e:
        print(f"Error checking wallet {wallet_address}: {e}")
        return wallet_address, None

def check_wallets_from_file(file_path):
    # Read wallet addresses from the fresh_wallets.txt file
    with open(file_path, 'r', encoding='utf-8') as f:
        wallets = f.readlines()

    # Trim any extra whitespace or newlines from each wallet address
    wallets = [wallet.strip() for wallet in wallets]

    # Check the balance for each wallet address
    results = []
    for wallet in wallets:
        result = check_wallet_balance(wallet)
        results.append(result)

    # Optionally, write the results to a new file
    with open("wallet_balances.txt", "w", encoding='utf-8') as result_file:
        for wallet, balance in results:
            result_file.write(f"{wallet}: {balance if balance is not None else 'Error'}\n")
    
    print("Results have been saved to wallet_balances.txt")

if __name__ == "__main__":
    # File path to the fresh_wallets.txt file on the Desktop
    file_path = r'C:\Users\pc\Desktop\fresh_wallets.txt'  # Modify the path as needed
    check_wallets_from_file(file_path)
