import csv 
import json
import re


RAW_CSV = "data/SNAP_Vendor_List.csv"

def parse_csv(raw_csv, delimiter):
	"""parses a csv into json-like object"""

	#open csv file
	opened_file = open(raw_csv)

	#read the data in the csv
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	#skip the first row and assign to var. (b/c those are the field names)
	fields = csv_data.next()

	store_type = {}

	for row in csv_data:

		formatted_items = split_addr_from_coords(row[2])

		#make sure the store type doesn't get repeated
		if row[3] not in store_type:
			store_type[row[3]] = []
		
		#for every record within a store type, create this dict
		vendor = {
			"Store Name" : row[1],
			"Address": formatted_items["address"],
			"Coordinates": formatted_items["coords"]
		}

		#add the vendor dict to the store type list
		store_type[row[3]].append(vendor) 

	#close the file
	opened_file.close()

	#return the parsed data
	return store_type

def split_addr_from_coords(address):
	#remove coords from address
	address_with_coords = address

	#use regex to find coords in address string
	regex = re.compile("\(.*\)")
	unformatted_coords = regex.findall(address_with_coords)

	#remove coords from addr
	cleaned_address = address_with_coords.replace(str(unformatted_coords[0]), "")
	cleaned_address = cleaned_address.replace("\n", " ")

	#remove parentheses and whitespace from coords and save coords to a variable
	cleaned_coords = re.sub(r"(\(|\)|\s)", "", unformatted_coords[0]).split()

	formatted_items = {
		"address": cleaned_address,
		"coords": cleaned_coords
	}

	return formatted_items

def main():
	parse_csv(RAW_CSV, ",")
	d = parse_csv(RAW_CSV, ",")
	with open("SNAP_Vendors.json", "w") as f:
		f.write(json.dumps(d))

if __name__ == "__main__":
    main()