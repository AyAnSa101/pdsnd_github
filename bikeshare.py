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
    city_list = ['chicago','new york city','washington']
    month_list = ['all','january','february','march','april','may','june']
    weekday_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    while True:
        city = input ("Please enter the city you would like to explore between the following choices: Chicago, New York City and Washington: ").lower()
        if city not in city_list:
            print("Your city input was incorrect!")
            continue
        else:

    # TO DO: get user input for month (all, january, february, ... , june)
            while True:
                month = input("Please enter the month (in full), you would like to explore. If you would like to explore all available months, please enter \'all\': ").lower()
                if month not in month_list:
                    print("Your month input was incorrect!")
                    continue
                else:

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                    while True:
                        day = input("Please enter the day of week (in full), you would like to explore. If you would like to explore all the days of the week, please enter \'all\': ").lower()
                        if day not in weekday_list:
                            print("Your weekday input was incorrect!")
                            continue
                        else:
                            break
                    break
            break
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
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    print("The most common month for trips was: {}".format(mode_month))

    # TO DO: display the most common day of week
    mode_weekday = df['day_of_week'].mode()[0]
    print("The most common day of the week for trips was: {}".format(mode_weekday))

    # TO DO: display the most common start hour
    mode_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour for trips was: {}".format(mode_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station was: {}".format(mode_start_station))

    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station was: {}".format(mode_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_trip_combo = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("The most frequest trip start station and end station combination was: {}".format(frequent_trip_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The average trip duration was: {}".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Here is a count of the different user types: {}".format(user_types))

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts().to_string()
    print("Here is a count of the trips taken by gender: {}".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    #df['Birth Year'] = pd.to_datetime(df['Birth Year'])
    early_birth_year = df['Birth Year'].min()
    recent_birth_year = df['Birth Year'].max()
    mode_yob = df['Birth Year'].mode()[0]

    print("The earliest,most recent and most common year of birth are the following: {}, {}, {}".format(early_birth_year,recent_birth_year,mode_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart the statistical analysis? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

# Displays the raw data, 5 rows at a time, if propmted by user
    while True:
        size = 0
        view_raw_data = input('\nWould you like to view the raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            break
        else:
            #print(df.head())
            print(df[size:size+5])

        while True:
            more_data = input('\nWould you to view more rows of the raw data? Enter yes or no.\n')
            size+=5
            if more_data.lower() != 'yes':
                break
            else:
                print(df[size:size+5])
        break


if __name__ == "__main__":
	main()
