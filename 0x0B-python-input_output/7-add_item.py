#!/usr/bin/python3
'''Module for providing a load, add and save functionality'''

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    '''Function to add all arguments passed upon execution of the script to a
    list and write them to a file'''
    try:
        import sys
        curr = load_from_json_file("add_item.json")
        if len(sys.argv) > 1:
            to_append = sys.argv[1:]
            append_to_list(curr, to_append)
            # to_save = json.dumps(curr)
            save_to_json_file(curr, "add_item.json")
    except FileNotFoundError:
        to_append = sys.argv[1:]
        save_to_json_file(to_append, "add_item.json")


def append_to_list(list_name, to_append):
    for el in range(len(to_append)):
        list_name.append(to_append[el])


add_item()
