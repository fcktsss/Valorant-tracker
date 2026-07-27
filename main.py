from pdb import main
import sys
import os
import logging
import requests

input_value = input("Please enter a tag: ")
from api import response
input_value = input_value.strip()
username, tag = input_value.split("#")
if input_value is None:
    print(f"player not found: {input_value}")
    print("Please enter a valid tag in the format 'username#tag'.")
    got = input("Do you want to continue? (y/n): ")
    if got.lower() == "n":
        print("Exiting the program.")
        sys.exit(0)
else :
    print(f"result: {response.json()}")
print("Script execution completed.")


main()

