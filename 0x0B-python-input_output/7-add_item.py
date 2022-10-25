#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    list_file = load_from_json_file("add_item.json")
except:
    list_file = []

arguments_list = sys.argv[1:]
for arg in arguments_list:
    list_file.append(arg)

save_to_json_file(list_file, "add_item.json")
