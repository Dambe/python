#!/usr/bin/python3

from datetime import datetime, timedelta


def print_timedelta_hours_minutes(time_delta):
    td_hours = time_delta.seconds // 3600
    td_minutes = (time_delta.seconds // 60) % 60
    return f"{td_hours}:{td_minutes:02d}"


if __name__ == "__main__":
    # get start time from user input
    t_input = input("Enter Check-In Time [hh:mm]: ")
    t_start = datetime.strptime(t_input, "%H:%M")

    # calculate theoretical end time w/ and w/o coffee break
    t_end_regular = t_start + timedelta(hours=8.5)
    t_end_coffee = t_end_regular + timedelta(minutes=15)
    print("regular clock out: ", t_end_regular.strftime("%H:%M"))
    print("include coffee: ", t_end_coffee.strftime("%H:%M"))

    # get current time
    t_now = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M")
    # calculate current working time
    t_working = t_now - t_start
    t_working_coffee = t_working
    # after working 6 hours, 30min are deducted automatically
    if t_working > timedelta(hours=6):
        t_working = t_working - timedelta(minutes=30)
        t_working_coffee = t_working - timedelta(minutes=15)
    # after working 9 hours, 15min are additionally deducted automatically
    if t_working > timedelta(hours=9):
        print("")
        print("!!! 9 hours passed, 15min break additionally deducted !!!")
        t_working = t_working - timedelta(minutes=15)
        t_working_coffee = t_working

    print("")

    print(f"hours worked: {print_timedelta_hours_minutes(t_working)}")
    print(f"incl. coffee: {print_timedelta_hours_minutes(t_working_coffee)}")

    print("")

    # calculate overtime
    if t_working >= timedelta(hours=8):
        t_over = t_working - timedelta(hours=8)
        print(f"overtime: {print_timedelta_hours_minutes(t_over)}")
    else:
        t_remaining = timedelta(hours=8) - t_working
        print(f"remaining: {print_timedelta_hours_minutes(t_remaining)}")

    if t_working_coffee >= timedelta(hours=8):
        t_over_coffee = t_working_coffee - timedelta(hours=8)
        print(f"w/coffee: {print_timedelta_hours_minutes(t_over_coffee)}")
    else:
        t_remaining_coffee = timedelta(hours=8) - t_working_coffee
        print(
            f"w/coffee remaining: {print_timedelta_hours_minutes(t_remaining_coffee)}"
        )
