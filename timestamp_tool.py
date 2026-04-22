from datetime import datetime

print("1. Timestamp to Date")
print("2. Date to Timestamp")

choice = input("Choose option: ")

if choice == "1":
    ts = int(input("Enter Unix timestamp: "))
    dt = datetime.fromtimestamp(ts)
    print("Date:", dt)

elif choice == "2":
    date_str = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("Timestamp:", int(dt.timestamp()))

else:
    print("Invalid choice")
