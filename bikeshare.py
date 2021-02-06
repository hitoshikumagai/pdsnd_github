import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nPlease input Chicago, New York City, Washington\n").lower()
    while city not in {'chicago','new york city','washington'} :
        city = input("\nPlease input Chicago, New York city, Washington\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nPlease input month All or month as a number January:1, February:2, March:3, April:4, May:5, June:6\n").lower()
    while month not in {'all', '1', '2', '3', '4', '5', '6'}:
        month = input("\nPlease input month All or month as a number January:1, February:2, March:3, April:4, May:5, June:6\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nPlease input day All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday\n").lower()
    while day not in {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}:
        day = input("\nPlease input day All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday\n").lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # print(df)
   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # filter by month to create the new dataframe
    if month != 'all':
        df = df[df['month'] == month]

    # extract month and day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """ Displays statistics on the most frequent times of travel.
        Flow Set dataframe with count -> Print
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_disp = df['month'].value_counts().index[0]
    print('\nMost Popular Month:', month_disp )
    
    # TO DO: display the most common day of week
    date_disp = df['day_of_week'].value_counts().index[0]
    print('\nMost Popular Day of Week:', date_disp)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_time_disp = df['hour'].value_counts().index[0]
    print('\nMost Popular Start Hour:', start_time_disp )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
           Flow Set dataframe with count -> Print
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().index[0]
    print('\nMost Popular Start station:', start_station )
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().index[0]
    print('\nMost Popular End station:', end_station )

    # TO DO: display most frequent combination of start station and end station trip
    combination =  df.iloc[ : , 4:6 ]
    combination = combination.mode()
    print('\nMost Popular Frequent Combination of Start Station and End Station trip:\n',combination)  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """ Displays statistics on the total and average trip duration.
        Flow Set dataframe with count -> Print
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration']
    total_travel = total_travel.dropna()
    total_travel = total_travel.sum()
    print('\nTotal Travel time:\n',total_travel)  
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration']
    mean_travel = mean_travel.dropna()
    mean_travel = mean_travel.mean()
    print('\nMean Travel time:\n',mean_travel)  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """ Displays statistics on bikeshare users.
        Flow Set dataframe with count -> Print
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type']
    user_types = user_types.dropna()
    user_types = user_types.value_counts()
    print('\nCounts User Types:\n',user_types)  

    if city != 'washington':
        # TO DO: Display counts of gender
        gender = df['Gender']
        gender = gender.dropna()
        gender = gender.value_counts()
        print('\nCounts Gender:\n',gender)  

        # TO DO: Display earliest, most recent, and most common year of birth
        year_of_birth= df['Birth Year']
        year_of_birth = year_of_birth.dropna()

        young = year_of_birth.min()
        old = year_of_birth.max()
        common = year_of_birth.mean()

        print('\nMost Recent Year of Birth:\n',young)  
        print('\nEarliest Year of Birth:\n',old)  
        print('\nMost Common Year of Birth:\n',common)  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    """  Changed:   user_stats(df) -> user_stats(df, city)  
         Root   :   Washington has no columns 'Gender' , 'Year of Birth'
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter Yes or No\n')
        start_loc = 0
        while (view_data != 'no'):
            print(df.iloc[start_loc:start_loc+5,:])
            start_loc += 5
            view_data = input('Do you wish to continue?:').lower() 
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
