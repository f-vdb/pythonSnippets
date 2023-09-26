import datetime

current_time_stamp = datetime.datetime.now().strftime(format("%Y%m%d_%H%M%S"))

# e.g. 20230926_134215
print(current_time_stamp)



def convert_seconds_to_datetime(seconds):
    return datetime.datetime.fromtimestamp(seconds)

seconds_since_epoch = 1695591900
date_time = convert_seconds_to_datetime(seconds_since_epoch)
print(f"Date and Time: {date_time}")


seconds_since_epoch = 1692618300
date_time = convert_seconds_to_datetime(seconds_since_epoch)
print(f"Date and Time: {date_time}")

seconds_since_epoch = 1692693900
date_time = convert_seconds_to_datetime(seconds_since_epoch)
print(f"Date and Time: {date_time}")
