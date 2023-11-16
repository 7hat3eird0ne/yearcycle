# Year Cycle Method
## Info
Hi, this is little project I have made in 2 days.

This is week day calculator - give it a date in DDMMYYYY format and it will calculate week day.

This started by thinking about patterns in years and its first days

Normaly each year first day is shifted by one, on leap years, it is shifted by additional day.

Based of that, I made cycle of 28 years, starting with year going right after leap year, starting in Monday.

So we only need to know when the cycle starts, and then by memorising all years we can get first day of year, and then offset it to whole date

But because 100, 200, 300 years are not actual leap years, the cycle is incomplete, but the complete cycle comes out to be 400 years old. JSON file featuring the whole list is avaiable in the release.

First, we don't have to memorise all 28 years, we can memorise only the leap years
    1. Offset to the last leap year
    1. Based of leap year, set it to week day
    1. Offset the week day back
    1. Add the additional day for leap year

So I have made the list of all initial Year Cycles, which based of them I search for leap years.

Now I got week day, so I found out how to shift days based of month to get first day of month

And after that, if the year is leap year and if month is not January or February

Last I will shift it again to match day

This is my "rough" explanation of this calculator.

## Method
1. If the current year isn't a leap year already, find out last leap year (including centuries, even though they are not leap years) from the current year and remember the offset
    - Note: leap year is always divisible by 4, although normaly centuries are never leap years unless divisble by 400, in this example lets pretend that there are each century is always a leap year, because later it will be much easier

1. Get a remainder of the last leap year by 400

1. Find a initial year in extended year cycle which is the largest year smaller than the remainder, if remainder is 0, initial year is 373
    - Extended Year Cycle Initial List:
        - Saturday part:
            - 1
            - 29
            - 57
            - 85
        - Friday part:
            - 125
            - 153
            - 181
        - Wednesday Part:
            - 221
            - 249
            - 277
        - Monday Part:
            - 317
            - 345
            - 373
    - Note: EYCIL is biggest struggle in memorisation, if you want to use this in pracice, memorise only one or two which you are going to use in next decade.

1. Do calculation "(remainder - initial year) / 4"

1.  Use the new number to get weekday of first day of the leap year you chose
    - Explanation for "Special Cycles":
        - Friday Cycle is for the initial year 85
        - Wednesday Cycle is for the initial year 181
        - Monday Cycle is for the initial year 277
    - Cycles to weekday list:
        - Saturday Cycle:
            - if new number is 1:
                - Leap year day is Thursday
            - if new number is 2:
                - Leap year day is Tuesday
            - if new number is 3:
                - Leap year day is Sunday
            - if new number is 4:
                - Leap year day is Friday
            - if new number is 5:
                - Leap year day is Wednesday
            - if new number is 6:
                - Leap year day is Monday
            - if new number is 7:
                - Leap year day is Saturday

        - Friday Cycle:
            - if new number is 1:
                - Leap year day is Thursday
            - if new number is 2:
                - Leap year day is Tuesday
            - if new number is 3:
                - Leap year day is Sunday
            - if new number is 4:
                - Leap year day is Friday
            - if new number is 5:
                - Leap year day is Tuesday
            - if new number is 6:
                - Leap year day is Sunday
            - if new number is 7:
                - Leap year day is Friday
            - if new number is 8:
                - Leap year day is Wednesday
            - if new number is 9:
                - Leap year day is Monday
            - if new number is 10:
                - Leap year day is Saturday
        
        - Wednesday Cycle:
            - if new number is 1:
                - Leap year day is Thursday
            - if new number is 2:
                - Leap year day is Tuesday
            - if new number is 3:
                - Leap year day is Sunday
            - if new number is 4:
                - Leap year day is Friday
            - if new number is 5:
                - Leap year day is Wednesday
            - if new number is 6:
                - Leap year day is Sunday
            - if new number is 7:
                - Leap year day is Friday
            - if new number is 8:
                - Leap year day is Wednesday
            - if new number is 9:
                - Leap year day is Monday
            - if new number is 10:
                - Leap year day is Saturday
        - Monday Cycle:
            - if new number is 1:
                - Leap year day is Thursday
            - if new number is 2:
                - Leap year day is Tuesday
            - if new number is 3:
                - Leap year day is Sunday
            - if new number is 4:
                - Leap year day is Friday
            - if new number is 5:
                - Leap year day is Wednesday
            - if new number is 6:
                - Leap year day is Monday
            - if new number is 7:
                - Leap year day is Friday
            - if new number is 8:
                - Leap year day is Wednesday
            - if new number is 9:
                - Leap year day is Monday
            - if new number is 10:
                - Leap year day is Saturday
        - Note 2: By "leap year day", I mean first day of the original leap year you chose.

1. Offset the leap year day by same amount of days into future that you originaly offset to get the leap year, this way you now got first day of the year
    - Note: offset to get the leap year in years = offset to get the first day in the original year

1. Offset the first day of year by speciffic amount of days
    - if current month is January:
        - first day offset is 0
    - if current month is February:
        - first day offset is 3:
    - if current month is March:
        - first day offset is 3
    - if current month is April:
        - first day offset is 6
    - if current month is May:
        - first day offset is 1
    - if current month is June:
        - first day offset is 4
    - if current month is July:
        - first day offset is 6
    - if current month is August:
        - first day offset is 2
    - if current month is September:
        - first day offset is 5
    - if current month is October:
        - first day offset is 0
    - if current month is November:
        - first day offset is 3
    - if current month is December:
        - first day offset is 5
    - Note: Again, memorisation of this list should be done only if planned to be used practicly, but if that's case, then it is much more importmant to memorise than EYCIL

1. If the current year is a leap year, and current month isn't January or February, offset the weekday by 1

1. Offset the weekday by remainder of the current day by 7

Congratulations, you have found the weekday of the date!