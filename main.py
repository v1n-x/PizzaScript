#!/usr/bin/python
import postparameters
import parsehtml
import requests
import sys
from datetime import datetime



# Display at the start of the program
separator = '###############################################################################\n\n'
intro = '    '
# -----------------------------------

def main():
	# Set up a log
	logtxt = ''
	log = open("log", "w")
	now = datetime.now()
	logtxt = logtxt + now.strftime("%d/%m/%y-%H:%M %A") + '\n'

	# Print intro banner
	print(intro)
	print(separator)

	# Gather address details
	# THIS NEEDS TO BE INPUT VALIDATED IN A LATER VERSION
	postparameters.params['Customer.UnitNo'] = input("Enter your Unit Number: ")
	postparameters.params['Customer.StreetNo'] = input("Enter your Street Number: ")
	postparameters.params['Customer.Street'] = input("Enter your Street Name: ")
	postparameters.params['Customer.Suburb'] = input("Enter your Suburb Name: ")
	postparameters.params['Customer.Postcode'] = input("Enter your Postcode: ")
	logtxt = logtxt + "\nAddress has been processed."
	logtxt = logtxt + "\n" + str(postparameters.params)

	# Start a connection, check status code
	r = requests.get(postparameters.delivery_url)
	r = requests.post(postparameters.delivery_posturl, postparameters.params, postparameters.request_headers)
	logtxt = logtxt + "\nPOST Request sent. Response: " + str(r)
	if not str(r) == "<Response [200]>":
		log.write(logtxt)
		log.close()
		sys.exit("Connection not accepted. Exiting...")

	# Parse the raw HTML and find the accurate address href
	postparameters.delivery_confirm_url = parsehtml.parseAddressHREF(r.text)

	# Connect to ordering menu
	r = requests.get(postparameters.site_base + postparameters.delivery_confirm_url)

	# END
	log.write(logtxt)
	log.close()
	sys.exit("Connection accepted. Exiting...")

if __name__ == '__main__':
	main()
