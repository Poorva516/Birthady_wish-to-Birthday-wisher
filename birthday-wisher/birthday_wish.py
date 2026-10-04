import csv
from datetime import datetime

def check_birthdays():
    today = datetime.now()
    today_month = today.month
    today_day = today.day
    
    found = False
    
    with open('birthdays.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # row = {'name': 'Aarav', 'month': '10', 'day': '4'}
            if int(row['month']) == today_month and int(row['day']) == today_day:
                print(f" Happy Birthday, {row['name']}! ")
                found = True
    
    if not found:
        print(f"Today is {today_day}/{today_month}. No birthdays today.")

check_birthdays()