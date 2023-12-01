import unittest
import datetime
from MeetupCalculator import MeetupCalculator


class TestMeetupCalculator(unittest.TestCase):
    def test_first_monday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2013, 3, "first", "Monday"), datetime.date(2013, 3, 4))

    def test_second_tuesday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "second", "Tuesday"),
                         datetime.date(2023, 4, 11))

    def test_third_wednesday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "third", "Wednesday"),
                         datetime.date(2023, 4, 19))

    def test_fourth_thursday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "fourth", "Thursday"),
                         datetime.date(2023, 4, 27))

    def test_last_friday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "last", "Friday"), datetime.date(2023, 4, 28))

    def test_fifth_saturday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "fifth", "Saturday"),
                         datetime.date(2023, 4, 29))

    def test_first_sunday(self):
        self.assertEqual(MeetupCalculator.calculate_meetup_date(2023, 4, "first", "Sunday"), datetime.date(2023, 4, 2))

    def test_fifth_monday_exception(self):
        with self.assertRaises(Exception) as context:
            MeetupCalculator.calculate_meetup_date(2022, 2, "fifth", "Monday")
        self.assertIn("There is no matching date for the fifth Monday in 2 2022.", str(context.exception))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
