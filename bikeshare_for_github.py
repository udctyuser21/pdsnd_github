import time
import pandas as pd
import numpy as np

# Import files with description
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'
            }

# Alternative for customer to enter and alternative number instead of string entries of the cities makes it more clear, easier and faster
# Alternative for city inc. numbers
city_input_alternative = { '1': 'chicago',
                     '2': 'new york city',
                     '3': 'washington'
                   }

# Another Alternative to select weekday names
weekday_input_alternative = { '1'        : 'monday',
             '2'        : 'tuesday',
             '3'        : 'wednesday',
             '4'        : 'thursday',
             '5'        : 'friday',
             '6'        : 'saturday',
             '7'        : 'sunday',
             'monday'   : 'monday',
             'tuesday'  : 'tuesday',
             'wednesday': 'wednesday',
             'thursday' : 'thursday',
             'friday'   : 'friday',
             'saturday' : 'saturday',
             'sunday'   : 'sunday',
           }

# Another Alternative to select month names
month_input_alternative = { '1'          : 1,
               '2'          : 2,
               '3'          : 3,
               '4'          : 4,
               '5'          : 5,
               '6'          : 6,
               'january'    : 1,
               'february'   : 2,
               'march'      : 3,
               'april'      : 4,
               'may'        : 5,
               'june'       : 6
             }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('For which city you wanna see the data? Please enter the number or city name: \n1 - Chicago \n2 - New York City \n3 - Washington\n').lower()
        if city in CITY_DATA:
            city = CITY_DATA[city]
            print()
            break
        elif city in city_input_alternative:
            city = city_input_alternative[city]
            city = CITY_DATA[city]
            print()
            break
        else:
            print('\nUps, a problem occured :-) \nPlease enter the number or the name of the city again\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        print('Select a month by number or name or type [all] for the whole content')
        month = input('1 - January \n2 - February \n3 - March \n4 - April \n5 - May \n6 - June\nall \n').lower()
        if month == 'all':
            month = 'all'
            print()
            break
        elif month in month_input_alternative:
            month = month_input_alternative[month]
            print()
            break
        else:
            print('\nUps, a problem occured :-) \nPlease enter the number or the name of the month again\nor enter [all] if you want to have a look over all\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Select a month by no. or name or type [all] for the whole content')
        day = input('1 - Monday \n2 - Tuesday \n3 - Wednesday \n4 - Thursday \n5 - Friday \n6 - Saturday \n7 - Sunday \nall \n').lower()
        if day == 'all':
            day = 'all'
            print()
            break
        elif day in weekday_input_alternative:
            day = weekday_input_alternative[day]
            print()
            break
        else:
            print('\nUps, a problem occured :-) \nPlease enter the number or the name of the day again\nor enter [all] if you want to have a look over all\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # Orginial data stored according to user inputs
    df= pd.read_csv(city)
    # Add new column for month and weekday name
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day_name() #.dt.weekday_name
     # filter by month if chosen
    if month != 'all':
        df = df.loc[df['month'] == month]
    else:
        df.drop(['month'], axis=1, inplace=True)
    # Filter by weekday if applicable
    if day != 'all':
        df = df.loc[df['weekday'] == day.title()]
    else:
        df.drop(['weekday'], axis=1, inplace=True)
    
    # for me as a developer to check the counted/selected lines of data vs raw data in the csv files and 
    # for the customer nice to know how many data he/she selected to analyze 
    no_of_lines = df['Start Station'].count()
    print("{} analysed lines of data".format(no_of_lines))
    print('-'*40)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating statistics on the most frequent times of travel\n')
    start_time = time.time()

    # Add new column for month and weekday name
    df['Start Time']    = pd.to_datetime(df['Start Time'])
    df['month']         = df['Start Time'].dt.month
    df['weekday']       = df['Start Time'].dt.day_name() # replaced .dt.weekday_name to dt.day_name
    df['hour']          = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    for key, value in month_input_alternative.items():
        if value == common_month:
            common_month_name = key
    print('The most common...')
    print("- month is: {}".format(common_month_name))

    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print("- day of the week for bicyle renting is: {}".format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("- hour for bicyle renting is: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating statistics on the most popular stations and trip\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common...')
    most_common_start_station = df['Start Station'].mode()[0]
    print('- start station is: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('- end station in bike renting is: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('- trip for bike renting is: {}'.format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating statistics on the total and average trip duration\n')
    start_time = time.time()

    # TO DO: display total travel time

    travel_time_total = df['Trip Duration'].sum()

    seconds_per_day      = 60 * 60 * 24
    seconds_per_hour     = 60 * 60
    seconds_per_minute   = 60
    
    # for easier reading: separate the the value in days, hours and minutes
    travel_time_days    = travel_time_total // seconds_per_day
    travel_time_hours   = (travel_time_total - (travel_time_days * seconds_per_day)) // seconds_per_hour
    travel_time_minutes = (travel_time_total - (travel_time_days * seconds_per_day) - (travel_time_hours * seconds_per_hour)) // seconds_per_minute

    print('The total travel time is {:.0f} days - {:.0f} hours - {:.0f} minutes'.format(travel_time_days, travel_time_hours, travel_time_minutes))
    
    # TO DO: display mean travel time
    travel_time_mean    = df['Trip Duration'].mean()/60
    print('The mean travel time is {:.2f} minutes'.format(travel_time_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating statistics on bikeshare users\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Use of the Build-in method value_counts to count the unique values there

    print("Display overview on user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Use of the Build-in method value_counts to count the unique values there
    print()
    try:
        print("Display overview on gender:")
        print(df['Gender'].value_counts())
    except KeyError:
        print("NO gender column available in the selected data")

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    print("Display overview on birth year statistics: ")
    try:
        min_birth_year = int(df['Birth Year'].min())
        max_birth_year = int(df['Birth Year'].max())
        pop_birth_year = int(df['Birth Year'].mode()[0])
        print('Oldest one > The minimum year of birth is {:.0f}  \nYoungest one > The maximum year of birth is {:.0f}\nMost popular one > The most common year of birth is {:.0f}'.format(min_birth_year, max_birth_year, pop_birth_year))
    except KeyError:
        print("NO birth year column available in the selected data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # needed to represent only raw data columns and not calculated columns in show_data_details
def get_chunk(dataframe: pd.DataFrame, chunk_size: int, start_row: int = 0):
    """Gets slice of dataframe by chunk size"""
    end_row  = min(start_row + chunk_size, dataframe.shape[0])

    return dataframe.iloc[start_row:end_row, :]

def show_data_details(df):
    """Shows lines of raw data"""
    chunk_size = 5
    raw_data_prompt = input("Would you like to see {} lines of raw data?\nY/N\n".format(chunk_size)).lower()
    start_row = 0
    while raw_data_prompt == 'y':
        chunk = get_chunk(df,chunk_size,start_row)
        chunk = chunk.iloc[:,1:8] # show only raw data columns and not calculated columns
        print(chunk)
        start_row += chunk_size
        raw_data_prompt = input("\nWould you like to see {} more lines of raw data?\nY/N\n".format(chunk_size)).lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data_details(df)

        restart = input('\nWould you like to restart?\nY/N\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()