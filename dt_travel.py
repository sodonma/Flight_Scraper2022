import datetime

class TravelDates:
    def __init__(self, departing = datetime.date.today(), finalday = datetime.date(2100, 1, 1)):
        self.start_date = departing
        self.end_date = finalday
    
    def TripDates(self, numdays = 4):

        start_date = self.start_date
        departures = []
        returning = []

        while start_date < self.end_date:
            # Adjust the end date from the start
            trip_len = start_date + datetime.timedelta(days=numdays)

            # Correctly format the MONTH to have a 0 in front
            if start_date.month < 10 :
                start_month = f'0{start_date.month}'
            else:
                start_month = start_date.month
            if trip_len.month < 10 :
                len_month = f'0{trip_len.month}'
            else: 
                len_month = trip_len.month
            # Correctly format the DAY to have a 0 in front
            if start_date.day < 10:
                start_day = f'0{start_date.day}'
            else:
                start_day = start_date.day
            if trip_len.day < 10 :
                len_day = f'0{trip_len.day}'
            else:
                len_day = trip_len.day

            # Correct the output to match the wedsite str requirements (YYYYMMDD)
            depart = f'{start_date.year}{start_month}{start_day}'
            returnd = f'{trip_len.year}{len_month}{len_day}'
            
            departures.append(depart)
            returning.append(returnd)
            # Adjust the start date by 1 day forward
            start_date = start_date + datetime.timedelta(days=1)
        return departures, returning
# FOR TESTING PURPOSES ONLY
x = TravelDates(departing= datetime.date.today(), finalday=datetime.date(2022, 10, 25)) #enter start date and final date
a, b = x.TripDates(5)
for i in range(len(a)):
    print(f'Departures: {a[i]} // Returns: {b[i]}')
# for i in range(3, 10): # range allows for trips 3 to 9 days for each start date
#     x.TripDates(i) #enter the number of trips last