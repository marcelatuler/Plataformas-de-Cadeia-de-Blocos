# -*- codingig: utf-8 -*-

import requests
import json


def main():
	rpcuser = 'node0'
	rpcpassword = 'node0'
	rpchost = 'localhost'
	rpcport = '8540'
	chainname = 'cadeia-multichain'
	auth = rpcuser+':'+rpcpassword
	
	url = 'http://127.0.0.1:8540/'
	headers = {'Host':rpchost,
            'Authorization': auth,
            'Content-type': 'application/json'
            }
	
	#params = {"method":"issue",
	#				"params":[{'address': ,
	#							'to': address_to,
	#							'gas': gas,
	#							'gasPrice': gas_price,
	#							'value': value
	#							}, 
	#						],
	#				"chain_name":"cadeia-multichain",
	#				"id":1,
	#				"jsonrpc":"2.0"
	#			}
	payload = {"method":"getpeerinfo",
					"params":[],
					"id":1,
					"jsonrpc":"2.0"
				}
	
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	
	if response.status_code == 200:
		print response.json()['result']
	else:
		print response.status_code
		print response.text
	
	
	
	
if __name__ == '__main__':
	main()