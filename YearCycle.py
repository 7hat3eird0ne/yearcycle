#memorisation stuff
EYCIL = [1, 29, 57, 85, 125, 153, 181, 221, 249, 277, 317, 345, 373]
MONTH_OFFSET = [0,3,3,6,1,4,6,2,5,0,3,5]
SATURDAY_CYCLE = [3,1,6,4,2,0,5]
FRIDAY_CYCLE = [3,1,6,4,1,6,4,2,0,5]
WEDNESDAY_CYCLE = [3,1,6,4,2,6,4,2,0,5]
MONDAY_CYCLE = [3,1,6,4,2,0,4,2,0,5]

def weekday(date):  
    #sets variables
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:-1] + date[-1])

    leap_year = year - year % 4 #1.

    remainder = leap_year % 400 #2.

    #3.
    if remainder == 0:
        remainder = 400
        initial_year = EYCIL[-1]
    else:
        for i in range(len(EYCIL)):
            if EYCIL[i] > remainder:
                initial_year = EYCIL[i - 1]
                break

    remainder = (remainder - initial_year + 1) // 4 #4.

    #5.
    if  initial_year == 85:
        weekday = FRIDAY_CYCLE[remainder - 1]
    elif initial_year == 181:
        weekday = WEDNESDAY_CYCLE[remainder - 1]
    elif initial_year == 277:
        weekday = MONDAY_CYCLE[remainder - 1]
    else:
        weekday = SATURDAY_CYCLE[remainder - 1]

    weekday += year % 4 #6.

    weekday += MONTH_OFFSET[month - 1] #7.

    #8.
    if ( (year - year % 4) % 400 == 0 or (year - year % 4) % 100 != 0 ) and ( year % 4 != 0 or month != 1 and month != 2 ):
        weekday += 1
        
    weekday += day % 7 - 1 #9. and 10.

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
    while True:
        date = input('DDMMYYYY... - ') #gets requested date
        weekday(date)