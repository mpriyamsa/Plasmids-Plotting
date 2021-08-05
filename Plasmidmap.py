import requests


class Plasmidmap:

    def __init__(self, my_dataframe, api_key):
        self.my_dataframe = my_dataframe
        self.api_key = api_key

    def get_location(self):
        latitudes = [], longitudes = []
        # For each address in data frame get latitude and longitude
        for elm in self.my_dataframe['Address']:
            geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(elm) + "&key={}".format(
                self.api_key)
            r = requests.get(geocode_url)
            results = r.json()['results']
            latitudes.append(results[0].get('geometry').get('location').get('lat'))
            longitudes.append(results[0].get('geometry').get('location').get('lng'))
        self.my_dataframe['Latitude'] = latitudes
        self.my_dataframe['Longitude'] = longitudes
        print(self.my_dataframe)
        # Write latitude and longitude data to csv
        self.my_dataframe.to_csv('New_Long_Lats.csv', index=False, mode='a', header=False)



