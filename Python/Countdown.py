import datetime

print("Hello! Please enter two dates and I will tell you the time between them!")

def valid_date(prompt):
    while True:
        date_input = input(prompt)
        try: 
            date=datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date
        except ValueError:
            print("Incorrect date format.")

date1 = valid_date("Date 1(YYYY-MM-DD)")
date2 = valid_date("Date 2(YYYY-MM-DD)")

date1_formatted = date1.date().strftime("%Y-%m-%d")
date2_formatted = date2.date().strftime("%Y-%m-%d")

print("Date 1 ", date1_formatted)
print("Date 2 ", date2_formatted)

delta = date2 - date1

days = delta.days

# print("There are " + str(days) + " days between " + str(date1) + " and " + str(date2))
# Use f-string to encapsulate the entire line of code as a string
output = f"There are {days} days between {date1_formatted} and {date2_formatted}"
print(output)