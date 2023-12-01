import datetime
import calendar


class MeetupCalculator:
    @staticmethod
    def calculate_meetup_date(year, month, week, day_of_week) -> datetime.date:
        # Convert day_of_week to a weekday number (0-6)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_num = days.index(day_of_week)

        # Find the first occurrence of the day in the month
        first_day_of_month = datetime.date(year, month, 1)
        first_day_of_week = first_day_of_month + datetime.timedelta(
            days=(day_num - first_day_of_month.weekday() + 7) % 7)

        # Calculate the final date based on the week descriptor
        if week in ["first", "second", "third", "fourth"]:
            weeks = {"first": 0, "second": 1, "third": 2, "fourth": 3}
            meetup_date = first_day_of_week + datetime.timedelta(weeks=weeks[week])
        elif week == "last":
            _, last_day_of_month = calendar.monthrange(year, month)
            last_day_of_month_date = datetime.date(year, month, last_day_of_month)
            meetup_date = last_day_of_month_date - datetime.timedelta(
                days=(last_day_of_month_date.weekday() - day_num + 7) % 7)
        elif week == "fifth":
            meetup_date = first_day_of_week + datetime.timedelta(weeks=4)
            if meetup_date.month != month:
                raise Exception(f"There is no matching date for the fifth {day_of_week} in {month} {year}.")
        else:
            raise ValueError("Invalid week descriptor")

        return meetup_date
