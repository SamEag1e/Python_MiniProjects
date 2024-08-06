"""Regex based functions to get required parts of string or text file.

Functions:
    iran_districts: Reads text files and returns districts dict object.
    phone_finder: Gets a string and extracts the phone numbers from it.
    email_finder: Gets a string and extracts the emails/gmails from it.
"""

import re
import os


def iran_districts(path="districts") -> dict:
    """Extract "en": "fa" dict for iran megacities districts.

    Args:
        path: the path for folder containing .txt files.
            (default: "districts")
    Returns:
        A dict containing all required data from all files.
    Reads text files placed in path directory and returns a dict
        based on them like this: {
            "tehran": {
                "abshar": "آبشار",
                ...
            },
            "ahvaz": {
                ....
            },
        }
    """

    city_pattern = r"districts_(\w+).txt"
    districts_pattern = r'buy-apartment/(\w+)">([^<]+)</a>'
    result = {}

    for file in os.listdir(path):
        with open(f"{path}/{file}", mode="r", encoding="utf-8") as f:

            result[re.findall(city_pattern, file)[0]] = dict(
                re.findall(districts_pattern, f.read())
            )

    return result


def phone_finder(text: str) -> list:
    """Gets a text and returns list of extracted phone numbers from it.

    Args:
        text: a string
    Returns:
        Phone numbers as list; Returns empty list if doesn't find any.
    """

    # My own thought.
    pattern = r"[0+]\d{10}"
    # Search results for unversal pattern = r'^\+?[1-9][0-9]{7,14}$'

    return re.findall(pattern, text)


def email_finder(text: str) -> list:
    """Gets a text and returns list of extracted e/gmails from it.

    Args:
        text: a string
    Returns:
        e/gmails as list; Returns empty list if doesn't find any.
    """

    # My own thought.
    pattern = r"[\s,:]([^\s,:]*@.*?\.[^\s,:]*)"
    # Search results for unversal:
    # pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    return re.findall(pattern, text)


# Test
# print(
#     email_finder(
#         "sdfsfs+9146446078 fdsafchera:samad@gmail.com jkdfkaefj omfg_jesus@yahoo.com"
#     )
# )

# Test result
# ['samad@gmail.com', 'omfg_jesus@yahoo.com']
print(iran_districts())
