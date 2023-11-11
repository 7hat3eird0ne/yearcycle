#memorisation stuff
EYCIL = [1, 29, 57, 85, 125, 153, 181, 221, 249, 277, 317, 345, 373]
WEEKDAY_NUMBERS = [3,1,6,4,2,0,5]
MONTH_OFFSET = [0,3,3,6,1,4,6,2,5,0,3,5]

def weekday(date):
    #sets variables
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:-1] + date[-1])

    leap_year = year - year % 4 #1.

    remainder = leap_year % 400 #2.

    #3.
    if remainder == 0:
        initial_year = EYCIL[-1]
    else:
        for i in range(len(EYCIL)):
            if EYCIL[i] > remainder:
                initial_year = EYCIL[i - 1]
                break

    remainder = (remainder - initial_year + 1) // 4 #4.

    weekday = WEEKDAY_NUMBERS[remainder - 1] #5.

    weekday += year % 4 #6.

    weekday += MONTH_OFFSET[month - 1] #7.

    #8.
    if year % 4 == 0 and month != 1 and month != 2:
        weekday += 1

    weekday += day % 7 #9.

    weekday %= 7 #Converting weekdays to cycles

    if weekday == 0:
        print('Monday')
        return 'Monday'
    elif weekday == 1:
        print('Tuesday')
        return 'Tuesday'
    elif weekday == 2:
        print('Wednesday')
        return 'Wednesday'
    elif weekday == 3:
        print('Thursday')
        return 'Thursday'
    elif weekday == 4:
        print('Friday')
        return 'Friday'
    elif weekday == 5:
        print('Saturday')
        return 'Saturday'
    else:
        print('Sunday')
        return 'Sunday'

if __name__ == '__main__':
    date = input('DDMMYYYY... - ') #gets requested date
    weekday(date)