"""This module finds duplicates in the given CSV file."""

import pandas as pd

print(
    """You need to have your data as a CSV file
    named data.csv in the same folder with this file.
    Your data shouldn't have any headers.
    This will return all values which were repeated in all columns"""
)
while True:
    number_of_columns = int(input("Enter Number of columns: "))

    try:
        data = pd.read_csv("data.csv", header=None)

        data_dict = {}
        for col in range(0, number_of_columns):
            data_dict[col] = []
        for col, data_list in data_dict.items():
            for item in data[col]:
                # KeyError if col number not correct
                if item not in data_list:
                    data_list.append(item)

        check = set()
        for col, data_list in data_dict.items():
            check |= {item for item in data_list}
        all_data = [item for items in data_dict.values() for item in items]
        if len(check) == len(all_data):
            print("No duplicate")
        else:
            duplicates = [
                item
                for item in all_data
                if all_data.count(item) == number_of_columns
            ]
            print(duplicates)
            with open(
                "result.csv", mode="w", encoding="utf-8", newline="\n"
            ) as f:
                for item in duplicates:
                    f.write(str(item) + ",")
    except Exception as e:
        print(
            """Something went wrong...
            Either you don't have the data.csv file in this directory...
            Or you didn't enter correct number of columns...
            Your data.csv file must have only datas you want to find
            duplicates in all columns of it...
            Also, the columns shouldn't have any header...
            Close the terminal, fix the possible issues and try again..."""
        )
    # End of exception
# End of while loop
