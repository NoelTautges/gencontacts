#!/usr/bin/env python3

import argparse
import csv
import itertools
import string
import sys

# I am fully aware that this is awful. I plan on changing it.
fieldnames = ["Title","First Name","Middle Name","Last Name","Suffix","Company","Department","Job Title","Business Street","Business Street 2","Business Street 3","Business City","Business State","Business Postal Code","Business Country/Region","Home Street","Home Street 2","Home Street 3","Home City","Home State","Home Postal Code","Home Country/Region","Other Street","Other Street 2","Other Street 3","Other City","Other State","Other Postal Code","Other Country/Region","Assistant's Phone","Business Fax","Business Phone","Business Phone 2","Callback","Car Phone","Company Main Phone","Home Fax","Home Phone","Home Phone 2","ISDN","Mobile Phone","Other Fax","Other Phone","Pager","Primary Phone","Radio Phone","TTY/TDD Phone","Telex","Account","Anniversary","Assistant's Name","Billing Information","Birthday","Business Address PO Box","Categories","Children","Directory Server","E-mail Address","E-mail Type","E-mail Display Name","E-mail 2 Address","E-mail 2 Type","E-mail 2 Display Name","E-mail 3 Address","E-mail 3 Type","E-mail 3 Display Name","Gender","Government ID Number","Hobby","Home Address PO Box","Initials","Internet Free Busy","Keywords","Language","Location","Manager's Name","Mileage","Notes","Office Location","Organizational ID Number","Other Address PO Box","Priority","Private","Profession","Referred By","Sensitivity","Spouse","User 1","User 2","User 3","User 4","Web Page"]

parser = argparse.ArgumentParser(description="Generate emails, phone numbers, or contacts for either.")
parser.add_argument("--email", help="the email template")
parser.add_argument("--phone", help="the phone number template")
parser.add_argument("--1", dest="s1", help="custom character set 1")
parser.add_argument("--2", dest="s2", help="custom character set 2")
parser.add_argument("--3", dest="s3", help="custom character set 3")
parser.add_argument("--4", dest="s4", help="custom character set 4")
parser.add_argument("--outfile", help="save the results to this file as a raw list")
parser.add_argument("--csv", help="save the results to this file as a Google Contacts- and Outlook-compatible contacts CSV")

def main():
	args = parser.parse_args()
	
	if not args.email and not args.phone:
		print("Error: must select email or phone")
		sys.exit(1)
	
	replace_dict = {}
	
	replace_dict["?l"] = string.ascii_lowercase
	replace_dict["?d"] = string.digits
	replace_dict["?a"] = string.ascii_lowercase + string.digits
	
	if args.s1:
		replace_dict["?1"] = args.s1
	if args.s2:
		replace_dict["?2"] = args.s2
	if args.s3:
		replace_dict["?3"] = args.s3
	if args.s4:
		replace_dict["?4"] = args.s4
	
	to_replace = args.email if args.email else args.phone
	index = to_replace.find("?")
	elements = []
	
	while index != -1:
		key = to_replace[index:index + 2]
		
		try:
			to_replace = to_replace.replace(key, "{}", 1)
			elements.append(replace_dict[key])
		except KeyError:
			print("Error: {} is not a valid key".format(key))
			sys.exit(1)
		
		index = to_replace.find("?")
	
	products = [to_replace.format(*product) for product in itertools.product(*elements)]
	
	if args.outfile:
		try:
			with open(args.outfile, "w") as outfile:
				for product in products:
					outfile.write(product + "\n")
		except IOError:
			print("Error: cannot open file {}".format(args.outfile))
			sys.exit(2)
	elif args.csv:
		try:
			with open(args.csv, "w") as contacts_file:
				contacts_csv = csv.DictWriter(contacts_file, fieldnames=fieldnames)
				contacts_csv.writeheader()
				
				for product in products:
					contacts_csv.writerow({"First Name": product, "E-mail Address": product if args.email else "", "Mobile Phone": product if args.phone else ""})
		except IOError:
			print("Error: cannot open file {}".format(args.csv))
			sys.exit(2)
	else:
		for product in products:
			print(product)

if __name__ == "__main__":
	main()
