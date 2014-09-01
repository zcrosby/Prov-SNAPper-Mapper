import csv 
import json
import re
from os import path, remove
from collections import defaultdict
import itertools

RAW_CSV = 'data/RI_Statewide_Vendors.csv'

#parses a csv and returna a list of obj
def parse_csv(raw_csv, delimiter):

	opened_file = open(raw_csv)
	data = csv.reader(opened_file, delimiter=delimiter)

	#skip column names
	column_names = data.next()

	stores = []

	for row in data:
		city_name = clean_city_name(row[5].title())

		formatted_address = row[3] + '. ' +  city_name + ' ' + row[6] + ' ' + row[7] + '-' + row[8]

		lat = float(row[2])
		long = float(row[1])
		coords = [lat , long] #[41.828739, -71.472778]

		store_info = {
						'Store Name': row[0].title(),
						'Address' : formatted_address.title().replace('Ri', 'RI'),
						'Coords' : coords,
						'County' : row[9].title(),
						'city': city_name
					}

		stores.append(store_info)

	return stores


def clean_city_name(city_name):

	if city_name == 'E Providence':
		city_name = 'East Providence'
	elif city_name == 'N Providence':
		city_name = 'North Providence'
	elif city_name == 'N Kingstown':
		city_name = 'North Kingstown'
	elif city_name == 'N Smithfield':
		city_name = 'North Smithfield'
	elif city_name == 'E Greenwich':
		city_name = 'East Greenwich'
	elif city_name == 'W Greenwich':
		city_name = 'West Greenwich'
	elif city_name == 'W Warwick':
		city_name = 'West Warwick'

	return city_name


def create_JSONLike_obj(store_list):
	stores = store_list

	#create a dict with list of cities
	stores_by_city = []

	#gather all cities 
	cities = []
	for s in stores:
		city = s['city'].title()
		cities.append(city)

	#remove duplicate citites
	non_dup_cities = []
	for c in cities:
		if c not in non_dup_cities:
			non_dup_cities.append(c)

	#each city gets a list of stores within that city
	for city in non_dup_cities:
		city_obj = {}
		city_obj['city'] = city
		city_obj['stores'] = []

		for s in stores:
			if s['city'] == city:
				store_info = {
						'Store Name': s['Store Name'],
						'Address' : s['Address'],
						'Coords' : s['Coords'],
						'County' : s['County']
					}
				city_obj['stores'].append(store_info)

		stores_by_city.append(city_obj)

	return stores_by_city


def write_to_file(obj):
	if path.isfile('Statewide_Vendors.json'):
		remove('Statewide_Vendors.json')
	else:
		with open('Statewide_Vendors.json', 'w') as f:
			f.write(json.dumps(obj))


def main():
	p = parse_csv(RAW_CSV, ',')
	j = create_JSONLike_obj(p)
	write_to_file(j)	

		
if __name__ == '__main__':
    main()