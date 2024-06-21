months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("Date: ").strip()
    
    if "/" in date_input:
        try:
            month, day, year = date_input.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass
    
    else:
        try:
            parts = date_input.replace(",", "").split()
            
            if len(parts) == 3:
                month_str, day, year = parts
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)

                if 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
        except (ValueError, IndexError):
            pass