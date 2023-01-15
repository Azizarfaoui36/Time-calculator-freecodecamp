
def NumberOfday(days):
    if (days == 1):
        return "(next day)"
    elif (days==0):
        return ""
    else:
        return "("+str(days)+" days later)"


daysWekk = [ "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",]


def add_time(start, duration, day=False):

    # decomposition of start
    start_hours = int(start.split(":")[0])
    start_min = int(start.split(":")[1].split(" ")[0])
    period = start.split(":")[1].split(" ")[1]

    # decomposition of duration
    duration_hours = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])
    if (duration_min >= 60):
        return "Error. duration minute must be less than 60"

    # calcul min
    end_min = start_min+duration_min

    if (end_min >= 60):
        duration_hours += 1
        end_min = end_min % 60

    # calcul total_hours
    total_hours = duration_hours+start_hours

    # calcul days
    days = 0
    if (total_hours >= 12):
        if (period == "AM"):
            days = (total_hours//24)
        else:
            days = (total_hours//24)+1

    # period
    temp_hours = total_hours
    while True:
        if temp_hours < 12:
            break
        if period == "AM":
            period = "PM"
        else:
            period = "AM"
        temp_hours -= 12

    remaining_hours = int(total_hours % 12)
    if(remaining_hours==0):
        remaining_hours=12
    remaining_mins = int(end_min % 60)

    #remaining_time
    remaining_time = f"{remaining_hours}:{remaining_mins:02} "+period

    #get_day
    if day:
        day = day.strip().lower()
        selected_day = int((daysWekk.index(day) + days) % 7)
        current_day = daysWekk[selected_day]
        remaining_time += f", {current_day.title()} {NumberOfday(days)}"

    else: 
        remaining_time +=" "+NumberOfday(days)

    #return
    return remaining_time.strip()
