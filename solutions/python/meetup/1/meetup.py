from datetime import date
import calendar

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    weekday = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    counter = 0
    last = calendar.monthrange(year, month)[1]

    if week == "first":
        for day in range(1,last+1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                return date(year, month, day)
    elif week == "second":
        for day in range(1,last+1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                if counter == 1:
                    return date(year, month, day)
                else:
                    counter += 1
    elif week == "third":
        for day in range(1,last+1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                if counter == 2:
                    return date(year, month, day)
                else:
                    counter += 1
    elif week == "fourth":
        for day in range(1,last+1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                if counter == 3:
                    return date(year, month, day)
                else:
                    counter += 1
    elif week == "fifth":
        for day in range(1,last+1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                if counter == 4:
                    return date(year, month, day)
                else:
                    counter += 1
    elif week == "last":
        for day in range(last, 0, -1):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                return date(year, month, day)
    elif week == "teenth":
        for day in range(13,20):
            if weekday[date(year, month, day).weekday()] == day_of_week:
                return date(year, month, day)
    raise MeetupDayException("That day does not exist.")