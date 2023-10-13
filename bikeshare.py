import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city would you like to see data for? New York, Washington, or Chicago: ")
        if city.lower() not in ('new york city', 'washington', 'chicago'):
            print("Invalid city name. Please try again.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ..., june)
    while True:
        month = input("\nWhich month would you like to see the data for? January, February, March, April, May, June, or type 'all': ")
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Invalid month name. Please try again.")
        else:
            break

    # TO DO: get user input for day of the week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day would you like to see the data for? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all': ")
        if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Invalid day name. Please try again.")
        else:
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip:', station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time (seconds):', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time (seconds):', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # TO DO: Display counts of gender (if available)
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:\n', gender_counts)
    else:
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth (if available)
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print('Earliest birth year:', int(earliest_birth_year))
        print('Most recent birth year:', int(most_recent_birth_year))
        print('Most common birth year:', int(common_birth_year))
    else:
        print('Birth year data is not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    #displays rows of data upon user request
    start_idx = 0
    chunk_size = 5

    while True:
        display = input('\nDo you want to see 5 rows of data? Enter yes or no: ')
        if display.lower() == 'yes':
            print(df.iloc[start_idx : start_idx + chunk_size])
            start_idx += chunk_size
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)  

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
