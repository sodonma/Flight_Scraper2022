import requests
import pandas as pd
from dt_travel import TravelDates as td
from datetime import date

"""Future goals for the program:
    1. Run multiple request at a single time
    2. Configure the request to one file
    3. include a range of trip lengths to go through 
        example: departures, returning = date_lists.TripDates(range(5, 10))
    4. Put into own folder
    5. Allow for an input function for depart/final dates as well as lengths of stay
"""


# setting up departure and return dates
date_lists =td(departing= date(2022, 9, 18), finalday= date(2022, 11, 30)) #use 'departing = date()' if first day isn't today
departures, returning = date_lists.TripDates(5) #Value in date_list = number days of trips
for i in range(len(departures)):
    url = "https://www.momondo.com/s/horizon/exploreapi/destinations"
    res =[]
    # variables to run through the querystring
    airport = 'NYC'
    depart = departures[i]
    returnd = returning[i]

    querystring = {"airport":airport,"budget":"",f"depart":depart,"return":returnd,"duration":"",
    "exactDates":"true","flightMaxStops":"0","stopsFilterActive":"true","topRightLat":"49.08943280266109",
    "topRightLon":"-60.540519040404206","bottomLeftLat":"31.23312586490063","bottomLeftLon":"-87.43505029040443",
    "zoomLevel":"4","selectedMarker":"","themeCode":"","selectedDestination":""}

    payload = ""
    headers = {
        "cookie": "Apache=Ska7Ig-AAABgrzaOJA-c5-XkO3Lg; kayak=pA5oov_Eju37w7eNfFY1; kmkid=ANme9eicsdxk_YHul6Sl_ms; csid=2c7984eb-137a-41b6-99c1-2d9c0bc34927; cluster=4; p1.med.sid=R-4Sgv2PZVn_3ie7aD3QABW-qS6IAiu4pkcSkaZYOBO2BQbBI2U2VbY5Qq2O2XfPv; kayak.mc=322^^-BtYaiDgQWIhvpbAebQDWCtP_IV3WpawX3bbJTTk2rfAoz3BL1A5VmXHBjqs859UKQw-LvR_i5vXjAMp6f7UrsD8AJdHUiTIxhSBo1YDDzc2fjdd-VRDRH45GiKeGLqDb1287_TAhnaYhTL8MW7Crpc95I-2gEJqTUeNGmDdpFy33rPgkTXjSDpxl5dBh0uKtI-eoWHyg; NSC_q4-tqbslmf=ffffffff094fbba345525d5f4f58455e445a4a422a59; g_state=^{^\^i_p^^:1661124216702,^\^i_l^^:2^}",
        "authority": "www.momondo.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "referer": f"https://www.momondo.com/explore/{airport}-anywhere/{depart},{returnd}?stops=0",
        "sec-ch-ua": "^\^Chromium^^;v=^\^104^^, ^\^"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    data = response.json()
    for p in data['destinations']:
        res.append(p)

    df = pd.json_normalize(res)
    df.to_csv(f'{airport}-NS-{depart}-{returnd}.csv')
    print(f"Code is complete dates {depart} // {returnd}!")