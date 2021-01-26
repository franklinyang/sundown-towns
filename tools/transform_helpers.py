import csv
import os


curr_dir = os.path.dirname(os.path.abspath(__file__))
# Returns a dict of cities mapped to county, eg: {'cambridge ma': 'Middlesex'}
def get_city_county_dict():
    city_county_dict = dict()
    with open(
        os.path.join(curr_dir, "../data/mapping_files/us_cities_to_county.csv")
    ) as city_mapping_file:
        city_mapping_reader = csv.DictReader(city_mapping_file)
        for c in city_mapping_reader:
            # need to add in state, otherwise get missed mappings
            city_county_dict[(c["city"] + " " + c["state_id"]).lower()] = c["county_name"]
    return city_county_dict


# Returns a county with state from a city, eg: Middlesex County, MA
def get_county_from_city(city, state, city_county_map):
    city_to_county_output = {}
    lookup_str = " ".join([city, state]).lower()
    if lookup_str in city_county_map.keys():
        return city_county_map[lookup_str]
    else:
        return "Missed mapping"
        # print("missed mapping: ", city, ",", state)
