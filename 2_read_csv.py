"""
script read links from csv file and start function to
create information about hotels from tripe advisor site
"""

import csv
from trip_advisor_rating import get_information_from_tripadvisor_about_hotel


def read_csv_by_column_number(path_to_file, column_number=0):
    # Open the CSV file
    with open(path_to_file, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # Skip the header row (if any)
        next(csv_reader)

        # Select the column index you want to read
        column_index = column_number  # Assuming you want to read the 3rd column (0-based indexing)

        # Iterate through the rows and print the values in the selected column
        for row in csv_reader:
            print(row[column_index])
            get_information_from_tripadvisor_about_hotel(row[column_index])
        # print(csv_reader)


if __name__ == '__main__':
    read_csv_by_column_number('/Users/evgeniy/Desktop/Turkish_hotels.csv', 1)
