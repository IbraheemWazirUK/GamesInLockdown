import requests
from xml.etree import ElementTree

def to_text(elem):
	if type(elem) is None or elem.text is None:
		return ""
	return elem.text
def search_charity(chairty_name):
	response = requests.get('http://graphapi.firstgiving.com/v2/list/organization?q=organization_name:*' + chairty_name + '*&page_size=20&page=1')
	root = ElementTree.fromstring(response.content)
	orgs = []
	for i in range(len(root[0])):
		charity_id = to_text(root[i][0])
		org_name = to_text(root[0][i][2])
		address = to_text(root[0][i][14])
		phone_no = to_text(root[0][i][15])
		url = to_text(root[0][i][17])
		mission_statement = to_text(root[0][i].find('mission_statement'))
		orgs.append((charity_id, org_name, address, phone_no, url, mission_statement))

def donate(amount, bill_to_addressline, bill_to_city, bill_to_state, bill_to_zip, bill_to_country, bill_to_email, bill_to_first_name, bill_to_last_name, bill_to_phone_no, cc_type, cc_number, cc_exp_date_year, cc_exp_date_month, cc_card_calidation_no, charity_id, description, pledge_id, remote_addr, donation_message, allow_email_contact):
	xml = "<donation> <amount>" + amount 
	+ "</amount><billToAddressLine1>" + bill_to_addressline[0] 
	+ "</billToAddressLine1> <billToAddressLine2>" + bill_to_addressline[1] 
	+ "</billToAddressLine2> <billToCity>" + bill_to_city  
	+ "</billToCity> <billToState> " + bill_to_state 
	+ "</billToState> <billToZip>" + bill_to_zip 
	+ "</billToZip> <billToCountry>" + bill_to_country 
	+ "</billToCountry> <billToEmail>" + bill_to_email 
	+ "</billToEmail> <billToFirstName>" + bill_to_first_name 
	+  "</billToFirstName> <billToLastName>" + TestLast 
	+ "</billToLastName> <ccCardValidationNum>" + cc_card_calidation_no
	+ "</ccCardValidationNum> <ccExpDateMonth>"  + cc_exp_date_month
	+ "</ccExpDateMonth> <ccExpDateYear>" + cc_exp_date_year
	+ "</ccExpDateYear> <ccNumber>" + cc_number
	+ "</ccNumber> <ccType>" + cc_type
	+ "</ccType> <charityId>" + charity_id
	+ "</charityId> <currencyCode>USD</currencyCode> <description>" + description
	+ "</description> <donationMessage>" +donation_message
	+ "</donationMessage> <pledgeId>" +pledge_id
	+ "</pledgeId> <remoteAddr>" + +remote_addr
	+ " </remoteAddr> <allowEmailContact>" + allow_email_contact
	+ "</allowEmailContact> </donation>"

	headers = {'Content-Type': 'application/xml'}
	response = requests.post('https://api.firstgiving.com/donation/creditcard', data=xml, headers=headers)
