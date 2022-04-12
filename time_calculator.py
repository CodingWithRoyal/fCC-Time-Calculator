def add_hrs(start, add, meridiem, debug=False):
    frmt = 12

    # new hours according to 12 hrs format
    hrsToReturn = start + (add % frmt)

    # set meridiem
    subset = add//frmt
    while subset > 0:
        meridiem = "PM" if meridiem.lower() == "am" else "AM"
        subset -= 1

    # difference in n days
    nDays = 0
    frmt = 24

    nDays = add//frmt

    # if hrs >= 12 change meridiem
    if hrsToReturn >= 12:
        # exceptional case
        hrsToReturn = hrsToReturn % 12

        meridiem = "PM" if meridiem.lower() == "am" else "AM"
        
        # increase day by 1 if its next day
        if meridiem == "AM":
            nDays += 1

    # if hrs == 0
    if hrsToReturn == 0:
        hrsToReturn = 12

    response = {"hours": hrsToReturn, "meridiem": meridiem, "nDays": nDays}

    return response

def add_time(start, duration, day=""):
    nDays = 0
    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    try:
        hrs = int(start.split(":")[0])
        mins = int(start.split(":")[1].split(" ")[0])
        mrdm = str(start.split(":")[1].split(" ")[1])

        hrsToAdd = int(duration.split(":")[0])
        minsToAdd = int(duration.split(":")[1])

        mins += minsToAdd

        # add mins to time
        if mins > 60:
            hrsToAdd += 1
        newMins = mins % 60
        mins = newMins

        # magic calculation
        addHours = add_hrs(hrs, hrsToAdd, mrdm)

        mrdm = addHours["meridiem"]
        hrs = addHours["hours"]
        nDays = addHours["nDays"]
        
        # day of week
        if day != "":
            day = day.title()
            indexOfDay = daysOfWeek.index(day)
            indexOfDay += nDays
            indexOfDay = indexOfDay % 7
            day = daysOfWeek[indexOfDay]

        # make mins and hrs double digit
        # hrs = str(f'{hrs:02}')
        mins = str(f'{mins:02}')
        
        hrs = str(hrs)
        # mins = str(mins)

        # final response
        new_time = hrs + ":" + mins + " " + mrdm

        if day != "":
            new_time += ", "+day

        if nDays > 1:
            new_time += " (" + str(nDays) + " days later)"
        elif nDays == 1:
            new_time += ' (next day)'

        return new_time
    except:
        print( "Invalid date format" )