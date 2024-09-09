import time

time = time.localtime()

epoch_time = 1.6663558573622e9
seconds_since_epoch = int(epoch_time)
scientific_notation = f"{epoch_time:.2e}"
print(f"Seconds since January 1, 1970: {seconds_since_epoch} or {scientific_notation} in scientific notation")  
month = time.tm_mon
if month == 1:
    montgh = "January"
elif month == 2:
    montgh = "February"
elif month == 3:
    montgh = "March"
elif month == 4:
    montgh = "April"
elif month == 5:
    montgh = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
elif month == 12:
    month = "December"
print(month, time.tm_mday, time.tm_year)