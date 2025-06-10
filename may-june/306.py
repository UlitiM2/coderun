import sys
import datetime

sys.stdin = open('306.txt')
inp = sys.stdin.readlines()
dict_months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
dict_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

for i in range(len(inp)):
    day, month, year = inp[i].split()
    month = dict_months[month]
    day, month, year = int(day), int(month), int(year)
    date = datetime.date(year, month, day)
    num_of_day = date.weekday()
    print(dict_days[num_of_day])

