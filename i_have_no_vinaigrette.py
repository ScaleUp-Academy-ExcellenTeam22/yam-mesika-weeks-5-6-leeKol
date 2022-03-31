import datetime
import random


def get_random_date() -> datetime:
    """
    The function receives from the user two dates that represent a range of dates,
    and returns a random date from the range.
    :return: a random date from the range of dates.
    """
    start_date = datetime.datetime.strptime(input("Please enter the range start date: "), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(input("Please enter the range end date: "), "%Y-%m-%d")
    return (start_date + datetime.timedelta(days=random.randrange((end_date - start_date).days))).date()


def is_monday(date: datetime) -> bool:
    """
    The function gets a date and checks if the date is Monday.
    :param date: The date under review.
    :return: Boolean: If the date is Monday- true, otherwise- false.
    """
    return date.weekday() == 0

if __name__ == '__main__':
    random_date = get_random_date()
    print(random_date)
    if is_monday(random_date):
        print("I have no vinaigrette!")
