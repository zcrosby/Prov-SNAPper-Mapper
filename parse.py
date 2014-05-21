import csv 
import json
import re


RAW_CSV = "data/SNAP_Vendor_List.csv"

def parse_csv(raw_csv, delimiter):
	"""parses a csv into json object"""

	#open csv file
	opened_file = open(raw_csv)

	#read the data in the csv
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	#skip the first row and assign to var. (b/c those are the field names)
	fields = csv_data.next()

	#create list to hold dicts
	parsed_data = []

	#iterate over each row and extract the data for each row
	#each row is placed in a dict
	#zip assigns the field name with a value for each row
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	#iterate over the parsed data and grab the coords from address w/regex
	#set the coords to a variable
	#add coords var as new key value pair to each dict
	counter = 0
	for row in parsed_data:
		counter += 1
		#remove coords from address
		address_with_coords = row["Address"]
		#print address_with_coords

		#use regex to find coords in address string
		regex = re.compile("\(.*\)")
		dirty_coords = regex.findall(address_with_coords)
		#print dirty_coords

		#remove coords from addr
		cleaned_address = address_with_coords.replace(str(dirty_coords[0]), "")
		row["Address"] = cleaned_address

		#remove parentheses and whitespace from coords and save coords to a variable
		cleaned_coords = re.sub(r"(\(|\)|\s)", "", dirty_coords[0]).split()

		#add a new key/value coords pair to each row
		row["coords"] = cleaned_coords

	print parsed_data[0]
	#close the file
	opened_file.close()

	#return the parsed data
	return parsed_data

def main():
	parse_csv(RAW_CSV, ",")
	#d = parse_csv(RAW_CSV, ",")
	#with open("SNAP_Vendors.json", "w") as f:
		#f.write(json.dumps(d))

if __name__ == "__main__":
    main()