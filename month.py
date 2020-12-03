#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program displays the month of the year that represents the number


def main():
    # this program displays the month of the year that represents the number

    # input
    month_number = int(input("Enter an integer(1-12): "))
    print("")

    # process & output
    if month_number == 1:
        print("January")
    elif month_number == 2:
        print("January")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("Error!Invalid month")


if __name__ == "__main__":
    main()
