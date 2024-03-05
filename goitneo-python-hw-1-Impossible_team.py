from datetime import datetime, timedelta, date
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data
    current_date = date.today()
    birthdays = defaultdict(list)

    # Iterate through users
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days >= 0 and delta_days < 7:
            day_of_week = (current_date + timedelta(days=delta_days)).strftime('%A')
            birthdays[day_of_week].append(name)

    # Print the result
    for day, celebrants in birthdays.items():
        print(f"{day}: {', '.join(celebrants)}")

# Example users list with birthdays
users = [
    {"name": "John Smith", "birthday": date(1990, 10, 31)},
    {"name": "Tesolkina Kateryna", "birthday": date(1990, 4, 12)},
    {"name": "Alex Marx", "birthday": date(1990, 10, 30)},
    {"name": "Natalia Tesolkina", "birthday": date(1940, 4, 12)},
    {"name": "Riedl Marlene", "birthday": date(1939, 1, 30)}
]

# Call the function with the users list to get birthdays for the next week
get_birthdays_per_week(users)