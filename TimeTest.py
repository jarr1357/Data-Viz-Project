from datetime import datetime, timedelta

Start = '2019/08/24 11:55:00 AM'
End = '2019/08/24 12:05:00 PM'

start_time = datetime.strptime(Start,'%Y/%m/%d %I:%M:%S %p')
end_time = datetime.strptime(End,'%Y/%m/%d %I:%M:%S %p')

time_list = []
time = start_time
print(time)

while time <= end_time:
    time_list.append(str(time.strftime('%Y/%m/%d %I:%M:%S %p')))
    time = time + timedelta(seconds = 1)

print(time_list)
