from dotenv import load_dotenv
import os
import json

CHAIN_ID = 942	# Pulsechain Testnet v3	
MAX_GAS = 2000000

# Send native token
def send_pulse(web3, private_key, sender_account, receiver_address, value, f):
	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": receiver_address,
	    "gasPrice": web3.eth.gas_price,
	    "gas": MAX_GAS,
	    "value": value,
	    "nonce": web3.eth.get_transaction_count(sender_account.address)
	}
	signed_tx = web3.eth.account.sign_transaction(raw_tx, private_key)
	tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	log = "Sending " + str(value) + " Beats to " + receiver_address + ", Tx Hash: " + web3.to_hex(tx_hash) + "\n"
	print(log)
	f.write(log)

# Send HEX PRC20 token
def send_hex(web3, private_key, sender_account, receiver_address, value, f):
	contract_address = "0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39"

	with open("hex_contract_abi.json") as json_file:
		info_json = json.load(json_file)
	token_abi = info_json
	contract = web3.eth.contract(contract_address, abi=token_abi)

	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": contract_address,
	    "gasPrice": web3.eth.gas_price,
	    "gas": MAX_GAS,
	    "value": "0x0",
	    "data": contract.encodeABI('transfer', args=(receiver_address, value)),
	    "nonce": web3.eth.get_transaction_count(sender_account.address)
	}
	signed_tx = web3.eth.account.sign_transaction(raw_tx, private_key)
	tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	log = "Sending " + str(value) + " Hearts to " + receiver_address + ", Tx Hash: " + web3.to_hex(tx_hash) + "\n"
	print(log)
	f.write(log)

# Send PLSX PRC20 token
def send_plsx(web3, private_key, sender_account, receiver_address, value, f):
	contract_address = "0x07895912f3AB0E33aB3a4CEFbdf7a3e121eb9942"

	with open("ierc20_abi.json") as json_file:
		info_json = json.load(json_file)
	token_abi = info_json["abi"]
	contract = web3.eth.contract(contract_address, abi=token_abi)

	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": contract_address,
	    "gasPrice": web3.eth.gas_price,
	    "gas": MAX_GAS,
	    "value": "0x0",
	    "data": contract.encodeABI('transfer', args=(receiver_address, value)),
	    "nonce": web3.eth.get_transaction_count(sender_account.address)
	}
	signed_tx = web3.eth.account.sign_transaction(raw_tx, private_key)
	tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	log = "Sending " + str(value) + " PLSX to " + receiver_address + ", Tx Hash: " + web3.to_hex(tx_hash) + "\n"
	print(log)
	f.write(log)

# Send MINT PRC20 token
def send_mint(web3, private_key, sender_account, receiver_address, value, f):
	contract_address = "0xd967edbc442185182A6bdF24f697D5f3599aC354"

	with open("ierc20_abi.json") as json_file:
		info_json = json.load(json_file)
	token_abi = info_json["abi"]
	contract = web3.eth.contract(contract_address, abi=token_abi)

	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": contract_address,
	    "gasPrice": web3.eth.gas_price,
	    "gas": MAX_GAS,
	    "value": "0x0",
	    "data": contract.encodeABI('transfer', args=(receiver_address, value)),
	    "nonce": web3.eth.get_transaction_count(sender_account.address)
	}
	signed_tx = web3.eth.account.sign_transaction(raw_tx, private_key)
	tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	log = "Sending " + str(value) + " MINT to " + receiver_address + ", Tx Hash: " + web3.to_hex(tx_hash) + "\n"
	print(log)
	f.write(log)