import json
import time
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC_URL = "https://testnetv2.pulserpc.io/rpc"
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CHAIN_ID = 940	# Pulsechain Testnet v2	
MAX_GAS = 2000000
SEND_INTERVAL = 5  # seconds

# Send native token
def send_pulse(receiver_address, value):
	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": receiver_address,
	    "gasPrice": web3.eth.gasPrice,
	    "gas": MAX_GAS,
	    "value": value,
	    "nonce": web3.eth.getTransactionCount(sender_account.address)
	}
	signed_tx = web3.eth.account.signTransaction(raw_tx, PRIVATE_KEY)
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	print("Sending " + str(value) + " Beats to " + receiver_address)
	print("Tx Hash: " + web3.toHex(tx_hash))


# Send HEX PRC20 token
def send_hex(receiver_address, value):
	contract_address = "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
	token_abi = [{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data1","type":"uint256"},{"indexed":true,"internalType":"bytes20","name":"btcAddr","type":"bytes20"},{"indexed":true,"internalType":"address","name":"claimToAddr","type":"address"},{"indexed":true,"internalType":"address","name":"referrerAddr","type":"address"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data2","type":"uint256"},{"indexed":true,"internalType":"address","name":"senderAddr","type":"address"}],"name":"ClaimAssist","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":true,"internalType":"address","name":"updaterAddr","type":"address"}],"name":"DailyDataUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":true,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"ShareRateChange","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data1","type":"uint256"},{"indexed":true,"internalType":"address","name":"stakerAddr","type":"address"},{"indexed":true,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"StakeEnd","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data1","type":"uint256"},{"indexed":true,"internalType":"address","name":"stakerAddr","type":"address"},{"indexed":true,"internalType":"uint40","name":"stakeId","type":"uint40"},{"indexed":true,"internalType":"address","name":"senderAddr","type":"address"}],"name":"StakeGoodAccounting","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":true,"internalType":"address","name":"stakerAddr","type":"address"},{"indexed":true,"internalType":"uint40","name":"stakeId","type":"uint40"}],"name":"StakeStart","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":true,"internalType":"address","name":"memberAddr","type":"address"},{"indexed":true,"internalType":"uint256","name":"entryId","type":"uint256"},{"indexed":true,"internalType":"address","name":"referrerAddr","type":"address"}],"name":"XfLobbyEnter","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"data0","type":"uint256"},{"indexed":true,"internalType":"address","name":"memberAddr","type":"address"},{"indexed":true,"internalType":"uint256","name":"entryId","type":"uint256"},{"indexed":true,"internalType":"address","name":"referrerAddr","type":"address"}],"name":"XfLobbyExit","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"allocatedSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"rawSatoshis","type":"uint256"},{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"},{"internalType":"address","name":"claimToAddr","type":"address"},{"internalType":"bytes32","name":"pubKeyX","type":"bytes32"},{"internalType":"bytes32","name":"pubKeyY","type":"bytes32"},{"internalType":"uint8","name":"claimFlags","type":"uint8"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"},{"internalType":"uint256","name":"autoStakeDays","type":"uint256"},{"internalType":"address","name":"referrerAddr","type":"address"}],"name":"btcAddressClaim","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes20","name":"","type":"bytes20"}],"name":"btcAddressClaims","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes20","name":"btcAddr","type":"bytes20"},{"internalType":"uint256","name":"rawSatoshis","type":"uint256"},{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"}],"name":"btcAddressIsClaimable","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes20","name":"btcAddr","type":"bytes20"},{"internalType":"uint256","name":"rawSatoshis","type":"uint256"},{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"}],"name":"btcAddressIsValid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"claimToAddr","type":"address"},{"internalType":"bytes32","name":"claimParamHash","type":"bytes32"},{"internalType":"bytes32","name":"pubKeyX","type":"bytes32"},{"internalType":"bytes32","name":"pubKeyY","type":"bytes32"},{"internalType":"uint8","name":"claimFlags","type":"uint8"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"claimMessageMatchesSignature","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"currentDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"dailyData","outputs":[{"internalType":"uint72","name":"dayPayoutTotal","type":"uint72"},{"internalType":"uint72","name":"dayStakeSharesTotal","type":"uint72"},{"internalType":"uint56","name":"dayUnclaimedSatoshisTotal","type":"uint56"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"beginDay","type":"uint256"},{"internalType":"uint256","name":"endDay","type":"uint256"}],"name":"dailyDataRange","outputs":[{"internalType":"uint256[]","name":"list","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"beforeDay","type":"uint256"}],"name":"dailyDataUpdate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"globalInfo","outputs":[{"internalType":"uint256[13]","name":"","type":"uint256[13]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"globals","outputs":[{"internalType":"uint72","name":"lockedHeartsTotal","type":"uint72"},{"internalType":"uint72","name":"nextStakeSharesTotal","type":"uint72"},{"internalType":"uint40","name":"shareRate","type":"uint40"},{"internalType":"uint72","name":"stakePenaltyTotal","type":"uint72"},{"internalType":"uint16","name":"dailyDataCount","type":"uint16"},{"internalType":"uint72","name":"stakeSharesTotal","type":"uint72"},{"internalType":"uint40","name":"latestStakeId","type":"uint40"},{"internalType":"uint128","name":"claimStats","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"merkleLeaf","type":"bytes32"},{"internalType":"bytes32[]","name":"proof","type":"bytes32[]"}],"name":"merkleProofIsValid","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"pubKeyX","type":"bytes32"},{"internalType":"bytes32","name":"pubKeyY","type":"bytes32"},{"internalType":"uint8","name":"claimFlags","type":"uint8"}],"name":"pubKeyToBtcAddress","outputs":[{"internalType":"bytes20","name":"","type":"bytes20"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"pubKeyX","type":"bytes32"},{"internalType":"bytes32","name":"pubKeyY","type":"bytes32"}],"name":"pubKeyToEthAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"stakerAddr","type":"address"}],"name":"stakeCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"stakeIndex","type":"uint256"},{"internalType":"uint40","name":"stakeIdParam","type":"uint40"}],"name":"stakeEnd","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"stakerAddr","type":"address"},{"internalType":"uint256","name":"stakeIndex","type":"uint256"},{"internalType":"uint40","name":"stakeIdParam","type":"uint40"}],"name":"stakeGoodAccounting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"stakeLists","outputs":[{"internalType":"uint40","name":"stakeId","type":"uint40"},{"internalType":"uint72","name":"stakedHearts","type":"uint72"},{"internalType":"uint72","name":"stakeShares","type":"uint72"},{"internalType":"uint16","name":"lockedDay","type":"uint16"},{"internalType":"uint16","name":"stakedDays","type":"uint16"},{"internalType":"uint16","name":"unlockedDay","type":"uint16"},{"internalType":"bool","name":"isAutoStake","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newStakedHearts","type":"uint256"},{"internalType":"uint256","name":"newStakedDays","type":"uint256"}],"name":"stakeStart","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"xfLobby","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"referrerAddr","type":"address"}],"name":"xfLobbyEnter","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"memberAddr","type":"address"},{"internalType":"uint256","name":"entryId","type":"uint256"}],"name":"xfLobbyEntry","outputs":[{"internalType":"uint256","name":"rawAmount","type":"uint256"},{"internalType":"address","name":"referrerAddr","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"enterDay","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"xfLobbyExit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"xfLobbyFlush","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"xfLobbyMembers","outputs":[{"internalType":"uint40","name":"headIndex","type":"uint40"},{"internalType":"uint40","name":"tailIndex","type":"uint40"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"memberAddr","type":"address"}],"name":"xfLobbyPendingDays","outputs":[{"internalType":"uint256[2]","name":"words","type":"uint256[2]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"beginDay","type":"uint256"},{"internalType":"uint256","name":"endDay","type":"uint256"}],"name":"xfLobbyRange","outputs":[{"internalType":"uint256[]","name":"list","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"}]
	contract = web3.eth.contract(contract_address, abi=token_abi)

	print(f"My HEX balance (before): {contract.functions.balanceOf(my_account.address).call()}")
	print(f"Receiver HEX balance (before): {contract.functions.balanceOf(receiver_address).call()}")
	
	raw_tx = {
	    "chainId": CHAIN_ID,   
	    "from": sender_account.address,
	    "to": contract_address,
	    "gasPrice": web3.eth.gasPrice,
	    "gas": MAX_GAS,
	    "value": "0x0",
	    "data": contract.encodeABI('transfer', args=(receiver_address, 1234567)),
	    "nonce": web3.eth.getTransactionCount(sender_account.address)
	}
	signed_tx = web3.eth.account.signTransaction(raw_tx, PRIVATE_KEY)
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	
	print("Tx Hash: " + web3.toHex(tx_hash))

	print(f"My HEX balance (after): {contract.functions.balanceOf(my_account.address).call()}")
	print(f"Receiver HEX balance (after): {contract.functions.balanceOf(receiver_address).call()}")

# Main
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if web3.isConnected():
	print("Web3 connected to " + RPC_URL) 
else:
	print("Web3 connect failed to " + RPC_URL)

sender_account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)

# Opening JSON file
with open('pulse.json') as json_file:
	data = json.load(json_file)

	for i in data['pulse_payout_addresses']:
		receiver = i['receiver']
		value = i['value']
		if not receiver or value == 0: 
			continue
		send_pulse(receiver, value)
		time.sleep(SEND_INTERVAL)
