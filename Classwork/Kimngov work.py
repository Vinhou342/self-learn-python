print("2025 Calendar")

months_31_days = ["January", "March", "May", "July", "August", "October", "December"]
months_30_days = ["April", "June", "September", "November"]
months_28_days = ["February"]

all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_of_week_counter = 2

for month in all_months:
    print(f"------------------------------")
    print(month)
    if month in months_31_days:
        num_days = 31
    elif month in months_30_days:
        num_days = 30
    elif month in months_28_days:
        num_days = 28
    for day in range(1, num_days + 1):
        weekday = days_of_week[day_of_week_counter % 7]
        print(day,weekday)
        day_of_week_counter += 1