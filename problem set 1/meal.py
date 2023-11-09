def main():
    time = (input("What time is it? (consider a 24h clock) ")).lower().strip().split(":")
    hour = float(time[0])
    minutes = float(time[1])
    time_converted = convert(hour, minutes)

    if(time_converted <= 8 and time_converted >= 7):
        print("breakfast time")
    elif(time_converted <= 13 and time_converted >= 12):
        print("lunch time")
    elif(time_converted <= 19 and time_converted >= 18):
        print("dinner time")
    else:
        print("it's not time for any meal")

def convert(hour, minutes):
    return  ((minutes/60) + hour)

main()