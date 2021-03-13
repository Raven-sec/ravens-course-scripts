#!/bin/python3
import json 
import requests
import socket 
import sys 


#Newline function for convenience
def nl():
	print("\n")

try:

	if len(sys.argv) < 2:
		print(f"Usage: python3 {sys.argv[0]} <URL> ")
		sys.exit(1)
	
	#Banner retrieval functionality - we supply URL via first argument
	req = requests.get(f"https://{sys.argv[1]}")
	nl()
	print(str(req.headers)) # Grabs response headers
	
	#Retrieves hostname
	gethostby_ = socket.gethostbyname(sys.argv[1])
	nl()
	print(f"The IP address of {sys.argv[1]} is {gethostby_}")
	nl()
	
	#IP Lookup
	#Gets lattitude + longitude by making a request to ipinfo.io API
	#Source: https://ipinfo.io/
	
	req_2 = requests.get(f"https://ipinfo.io/{gethostby_}/json") #Sends a get request in json format
	resp_ = json.loads(req_2.text) #Loads the request in JSON format, for API compatibility
	#Geolocational variables
	print(f"Location: {resp_['loc']}")
	print(f"Region: {resp_['region']}")
	print(f"City: {resp_['city']}")
	print(f"Country: {resp_['country']}")
	print(f"Timezone: {resp_['timezone']}")
	nl()
	
#Clean exit on keyboard interupt
except KeyboardInterrupt:
	print(f"Ctrl +Z detected, Exiting {sys.argv[0]}...")
	sys.exit(1)


