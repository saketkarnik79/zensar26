
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo

# Step 1: Current date and time
today = date.today()
now = datetime.now()

print("Current Date:", today)
print("Current Date and Time:", now)

# Step 2: Create a specific date
order_date = date(2026, 11, 12)

print("\nOrder Date:", order_date)

# Step 3: Convert string to datetime
date_string = "2026-11-12 10:30:00"

parsed_date = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

print("Parsed Date:", parsed_date)

# Step 4: Format date
formatted_date = parsed_date.strftime(
    "%d-%m-%Y"
)

print("Formatted Date:", formatted_date)

# Step 5: Extract date components
print("Year:", parsed_date.year)
print("Month:", parsed_date.month)
print("Day:", parsed_date.day)
print("Hour:", parsed_date.hour)
print("Minute:", parsed_date.minute)
print("Weekday:", parsed_date.strftime("%A"))

# Step 6: Date arithmetic
delivery_date = order_date + timedelta(days=5)

print("\nExpected Delivery:", delivery_date)

# Step 7: Difference between dates
start_date = date(2026, 11, 1)
end_date = date(2026, 11, 12)

difference = end_date - start_date

print("Difference in Days:", difference.days)

# Step 8: Time zone conversion
utc_time = datetime(
    2026, 11, 12, 10, 30,
    tzinfo=ZoneInfo("UTC")
)

india_time = utc_time.astimezone(
    ZoneInfo("Asia/Kolkata")
)

print("\nUTC Time:", utc_time)
print("India Time:", india_time)
