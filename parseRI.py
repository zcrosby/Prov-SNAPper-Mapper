import csv 
import json
import re
from os import path, remove

RAW_CSV = "data/RI_Statewide_Vendors.csv"

def parse_csv(raw_csv, delimiter):

	#open csv file
	opened_file = open(raw_csv)

	#read the file
	data = csv.reader(opened_file, delimiter=delimiter)

	#skip first line, which are the column names
	column_names = data.next()

	#create a dict to order stores by city
	city_stores = {}

	#build data structure
	for row in data:
		if row[5] not in city_stores:
			city_stores[row[5]] = []

		#format address
		formatted_address = row[3] + ". " +  row[5] + " " + row[6] + " " + row[7] + "-" + row[8]

		#format coords, put coords in a list
		lat = float(row[2])
		long = float(row[1])
		coords = [lat , long] #[41.828739, -71.472778]

		#create a data stucture to place store info into
		store_info = {
						"Store Name": row[0].title(),
						"Address" : formatted_address,
						"Coords" : coords,
						"County" : row[9].title()
					}

		#add the store info to its associated city
		city_stores[row[5]].append(store_info)

	return city_stores

def main():
	#parse_csv(RAW_CSV, ",")

	d = parse_csv(RAW_CSV, ",")

	if path.isfile("Statewide_Vendors.json"):
		remove("Statewide_Vendors.json")
	else:
		with open("Statewide_Vendors.json", "w") as f:
			f.write(json.dumps(d))

if __name__ == "__main__":
    main()