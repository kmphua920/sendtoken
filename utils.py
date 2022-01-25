from dotenv import load_dotenv
import os
import json

CHAIN_ID = 940	# Pulsechain Testnet v2	
MAX_GAS = 2000000

# Send native token
def send_pulse(web3, private_key, sender_account, receiver_address, value, f):
	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": receiver_address,
	    "gasPrice": web3.eth.gasPrice,
	    "gas": MAX_GAS,
	    "value": value,
	    "nonce": web3.eth.getTransactionCount(sender_account.address)
	}
	signed_tx = web3.eth.account.signTransaction(raw_tx, private_key)
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	log = "Sending " + str(value) + " Beats to " + receiver_address + ", Tx Hash: " + web3.toHex(tx_hash) + "\n"
	print(log)
	f.write(log)

# Send HEX PRC20 token
def send_hex(web3, private_key, sender_account, receiver_address, value, f):
	contract_address = "0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39"

	with open("hex_contract_abi.json") as f:
		info_json = json.load(f)
	token_abi = info_json
	contract = web3.eth.contract(contract_address, abi=token_abi)

	print(f"My HEX balance (before): {contract.functions.balanceOf(sender_account.address).call()}\n")
	print(f"Receiver HEX balance (before): {contract.functions.balanceOf(receiver_address).call()}\n")
	
	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": contract_address,
	    "gasPrice": web3.eth.gasPrice,
	    "gas": MAX_GAS,
	    "value": "0x0",
	    "data": contract.encodeABI('transfer', args=(receiver_address, value)),
	    "nonce": web3.eth.getTransactionCount(sender_account.address)
	}
	signed_tx = web3.eth.account.signTransaction(raw_tx, private_key)
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	
	print("Tx Hash: " + web3.toHex(tx_hash) + "\n")

	print(f"My HEX balance (after): {contract.functions.balanceOf(sender_account.address).call()}\n")
	print(f"Receiver HEX balance (after): {contract.functions.balanceOf(receiver_address).call()}\n")