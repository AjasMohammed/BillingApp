import calendar
from datetime import datetime, timedelta
import sqlite3

x = datetime.today().year
print(x)

current_date = datetime.today()
    # Calculate the start of the current week (Monday)
start_of_week = current_date - timedelta(days=current_date.weekday())
  # Calculate the end of the current week (Sunday)
end_of_week = start_of_week + timedelta(days=6)

start_of_month = current_date.replace(day=1)
end_of_month = start_of_month + timedelta(days=calendar.monthrange(start_of_month.year, start_of_month.month)[1])
print(start_of_month)
print(end_of_month)


print(start_of_week)
print(end_of_week)

conn = sqlite3.connect('C:\\Users\\Rahul\\Pybill\z\\bill_info.db')
cur = conn.cursor()
q=("""
                SELECT DATE(created_date) AS week_number, SUM(total) FROM bill_info 
                WHERE created_date BETWEEN ? AND ?
                GROUP BY DATE(created_date) 
                ORDER BY created_date
            """)
# cur.execute('SELECT DATE(created_date), SUM(total) FROM bill_info WHERE created_date BETWEEN ? AND ? GROUP BY DATE(created_date) ORDER BY DATE(created_date)', (start_of_month, end_of_month))
cur.execute(q, (start_of_month, end_of_month))
x = cur.fetchall()

def date_calc(week_number, year=2023):
    # Find the first day of the year
    first_day = datetime(year, 1, 1)

    # Find the first day of the week (Monday) of the given week number
    days_to_add = (week_number - 1) * 7
    first_day_of_week = first_day + timedelta(days=days_to_add)

    # Find the last day of the week (Sunday) of the given week number
    last_day_of_week = first_day_of_week + timedelta(days=6)

    f = first_day_of_week.strftime('%Y-%m-%d')
    l = last_day_of_week.strftime('%Y-%m-%d')

    return f, l

m= []
price = []
t = {}
for i in x :
    p = i[1]
    price.append(p)
    week = datetime.strptime(i[0], '%Y-%m-%d')
    m.append(week)
    x = datetime.isocalendar(week)[1]
    print("date",date_calc(x))
    if x not in t:
        t[x] = p
    else:
        t[x]+=p

    # week_number = i[0].weekday() 
print(start_of_month+timedelta(days=calendar.monthrange(start_of_month.year, start_of_month.month)[1]))
print(t)
