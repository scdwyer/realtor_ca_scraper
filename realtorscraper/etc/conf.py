'''
config for geographic locations, api calls, geographic decomposition
'''
import sys
import os.path

# TEMP, change
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'data')
LOCATIONS = {
        # add your (rectangular) geographic boundaries here
        'montreal': {
            'LONGITUDE_MIN' : '-74.3344106936035',
            'LONGITUDE_MAX' : '-72.91992094750975',
            'LATITUDE_MIN' : '45.28464264953363',
            'LATITUDE_MAX' : '45.77240489650948',
        },
        'okotoks': {
            'LONGITUDE_MIN' : '-114.05998',
            'LONGITUDE_MAX' : '-113.87013',
            'LATITUDE_MIN' : '50.69499',
            'LATITUDE_MAX' : '50.75378',
        }
}

    # adapt if US desired
API_URL = 'https://api2.realtor.ca/Listing.svc/PropertySearch?'
    # used as tolerance param on our grid decomposition of rectangular geographic boundaries
EPSILON = 0.0001

#WAIT_TIME = 30 #was not needed in cases used
#WAIT_FREQ = 10000

# https://www.realtor.ca/map#ZoomLevel=13&Center=50.724390%2C-113.965055&LatitudeMax=50.75378&LongitudeMax=-113.87013&LatitudeMin=50.69499&LongitudeMin=-114.05998&Sort=1-A&PGeoIds=g40_c3nbwdhd&GeoName=Okotoks%2C%20AB&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD
