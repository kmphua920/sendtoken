from web3 import Web3
from datetime import datetime
from dotenv import load_dotenv
import json
import time
import utils
import os

load_dotenv()

RPC_URL = "https://rpc.v2b.testnet.pulsechain.com"
PRIVATE_KEY = os.getenv('PRIVATE_KEY_PLSX_POOL_2')
SEND_INTERVAL = 10  # seconds

now = datetime.now()
log_file_name = now.strftime("%Y%m%d_%H:%M:%S.log")
web3 = Web3(Web3.HTTPProvider(RPC_URL))
sender_account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)

f = open(log_file_name, 'w')

# Opening JSON file
with open('plsx2.json') as json_file:
	data = json.load(json_file)

	for i in data['plsx_payout_addresses']:
		receiver = i['receiver']
		value = i['value']
		if not receiver or value == 0: 
			continue
		utils.send_plsx(web3, PRIVATE_KEY, sender_account, web3.toChecksumAddress(receiver), int(value), f)
		time.sleep(SEND_INTERVAL)

f.close()
