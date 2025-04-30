# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: April 29, 2025
# This program shows five numbers per line from 1000 until 2000
# It uses one For loop and one if statement inside


def main():
    # Loop through numbers from 1000 to 2000
    for integer in range(1000, 2001):

        # Display the current integer and then show a blank space
        print(integer, end=" ")

        # If the current integer remainder, after being divided by 5 equals 0 it will go to the next line
        # This is so it only prints five numbers in one line
        if integer % 5 == 0:
            print("")


if __name__ == "__main__":
    main()
