import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

testing = ['adding', 'info']

def get_filters(): #User inputs
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data together as a team!')

    while True: # User input for City
        city = input('Please enter the City you would like to view (make sure it is one of the three: chicago, new york city or washington) ')
        city = city.lower()
        if city == 'chicago' or city == 'new york city'  or city == 'washington':
            break
        print("Please check your spelling or enter a correct city and try again") 
    
    while True: #User input for month
        month = input('Please enter the month between January and June to filter by, or enter "all" to apply no month filter:  ')
        month = month.lower()
        
        if month in months and month!= 'all':
            month = months.index(month) + 1
            
            break
        elif month == 'all':
            break
        print("Please check your spelling or enter a correct month and try again") 
        
    while True: #User input for day
        day = input('Please enter the day of the week to filter by, or enter "all" to apply no day filter:  ')
        day = day.lower()
        
        if day in days:
            break
        print("Please check your spelling and try again")         
       
    return city, month, day
    
  
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
 
    df = pd.read_csv(CITY_DATA[city])
    
    #df.fillna(method = 'ffill', axis = 1) if i wanted to fill in empty values but this step added significant loading time

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        df = df[df['month'] == month]
        # filter by month to create the new dataframe

        
        # filter by day of week 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        # filter by day of week to create the new dataframe
        
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    #display the most common month
    
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    popular_month = df['month'].mode()[0]
   
    
    print('The most common month was: ', months[popular_month - 1])

    #display the most common day of week
    
    print('The most common Day of the week was: ', popular_day )


    #display the most common start hour
    
    print('The most common start hour was: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    df['Combo Station'] = df['Start Station'] + ' & ' +  df['End Station']
    popular_Start_Station = df['Start Station'].mode()[0]
    popular_End_Station = df['End Station'].mode()[0]
    popular_Combo_Station = df['Combo Station'].mode()[0]
    
    
    #popular_combo_station = df['Start Station']['End Station'].mode()[0]

    #display most commonly used start station
    
    print('The most common Start station was: ', popular_Start_Station )
    


    #display most commonly used end station
    
    print('The most common Start station was: ', popular_End_Station )


    #display most frequent combination of start station and end station trip
    
    print('The most common combination of start station and end station trip: ', popular_Combo_Station )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    
    total_seconds = df['Trip Duration'].sum()
    
    minutes = total_seconds // 60

    # Get additional seconds with modulus
    seconds = total_seconds % 60

    # Create time as a string
    time_string = "{},{}".format(minutes, seconds)
    
    print ('Total Travel time in minutes is exactly: ', time_string, "which in weeks is roughly around: ", total_seconds/60/60/24/7)
    


    #display mean travel time
    print ('mean of Travel time in seconds is: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    
    print("the count of the different user types are: \n", df['User Type'].value_counts())
    print()


    
    if 'Gender' in df:
        #Display counts of gender
        
        print("the count within the different Gender types are: \n", df['Gender'].value_counts())
        print()
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is ", df['Birth Year'].min())
        print("The Most Common year of birth is ", df['Birth Year'].mode()[0])
        print("The Most Recent year of birth is ", df.iat[0,8])
        
    
    
    



    print("\nThis took %s seconds." % (time.time() - start_time))     
    print('-'*40)

    
def Display_data(df):
    count = 0
    
    while True:
        data_summary = input("\nWould you like to view the first 5 rows of data of the dataset?  " )
        data_summary = data_summary.lower()
        
        if data_summary == "yes":
            print(df.iloc[count: count+5])
            count = count+5
            data_summary =input("\nDo you wish to continue?: " )
        if data_summary == "no":
            break
        elif data_summary != "yes" and data_summary != "no":
            print("\nPlease make sure you answered with either yes or no")
    
    

def main():
    
    y = True
    while y == True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        Display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        x = True
        
        while x == True:

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'no':            
                y = False
                break
               
        
            if restart.lower() == 'yes':  
                x = False
                
        
            elif restart.lower() != 'yes' or restart.lower() != 'no':
                print('Please make sure you only enter in the option "yes" or the option "no"')

if __name__ == "__main__":
	main()
