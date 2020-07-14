# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:
def update_damages(data):
    updated_damages = []
    factor = {"M": 10 ** 6, "B": 10 **9}
    for entry in data:
        if entry == "Damages not recorded":
            updated_damages.append(entry)
            continue
        updated_entry = float(entry.strip("MB")) * factor[entry.strip("0123456789.")]
        updated_damages.append(updated_entry)
    return updated_damages

updated_damages = update_damages(damages)
#print(updated_damages)


# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(n = names, m = months, y = years, msw = max_sustained_winds, a = areas_affected, dmg = updated_damages, d = deaths):
    hurricanes = {}
    for i in range(0, len(n)):
        hurricanes[n[i]] = {"Name": n[i], "Month": m[i], "Year": y[i], "Max Sustained Wind": msw[i], "Areas Affected": a[i], "Damage": dmg[i], "Deaths": d[i]}
    return hurricanes

hurricanes_by_name = construct_hurricane_dictionary()
#print(hurricanes_by_name["San Felipe II Okeechobee"])


# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(hurricanes_dct = hurricanes_by_name):
    hurricanes = {}
    for name, details in hurricanes_dct.items():
        if details["Year"] in hurricanes.keys():
            hurricanes[details["Year"]].append(details)
            continue
        hurricanes[details["Year"]] = [details]
    return hurricanes

hurricanes_by_year = hurricanes_by_year()
#print(hurricanes_by_year[1933])


# write your count affected areas function here:
    # Without using the dictionary:
'''
def count_areas_affected(areas = areas_affected):
    areas_list = []
    area_count = {}
    for lst in areas:
        for area in lst:
            areas_list.append(area)
    for area in areas_list:
        area_count[area] = areas_list.count(area)
    return area_count
'''
    # Using the dictionary
def count_areas_affected(hurricanes = hurricanes_by_name):
    areas_count = {}
    for hurricane in hurricanes.values():
        for area in hurricane["Areas Affected"]:
            if area in areas_count:
                areas_count[area] += 1
                continue
            areas_count[area] = 1
    return areas_count

areas_affected_count =  count_areas_affected()
#print(areas_affected_count)


# write your find most affected area function here:
def most_affected_area(areas_dict = areas_affected_count):
    highest_count = 0
    highest_area = ""
    for area, count in areas_dict.items():
        if count < highest_count:
            continue
        highest_count = count
        highest_area = area
    return highest_area, highest_count

most_affected_area, most_affected_count = most_affected_area()
#print(most_affected_area, str(most_affected_count))


# write your greatest number of deaths function here:
def greatest_deaths(hurricanes = hurricanes_by_name):
    highest_deaths = 0
    highest_name = ""
    for name, details in hurricanes.items():
        if details["Deaths"] < highest_deaths:
            continue
        highest_deaths = details["Deaths"]
        highest_name = name
    return highest_name, highest_deaths

greatest_deaths_name, greatest_deaths_count = greatest_deaths()
#print(greatest_deaths_name, greatest_deaths_count)


# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricanes = hurricanes_by_name):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes.values():
        if hurricane["Deaths"] > mortality_scale[4]:
            hurricanes_by_mortality[5].append(hurricane)
        for i in range(0, 4):
            if mortality_scale[i] < hurricane["Deaths"] <= mortality_scale[i+1]:
                hurricanes_by_mortality[i+1].append(hurricane)
    return hurricanes_by_mortality

hurricanes_by_mortality = categorize_by_mortality()
#print(hurricanes_by_mortality[4])


# write your greatest damage function here:

# write your catgeorize by damage function here:
