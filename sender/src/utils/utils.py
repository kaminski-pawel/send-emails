import csv
import json
import os


def open_json_file(filename):
    return _error_handler(filename, _open_json_file)

def open_html_file(filename):
    return _error_handler(filename, _open_html_file)

def open_csv_file(filename):
    return _error_handler(filename, _open_csv_file)

def _open_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def _open_html_file(filename):
    with open(filename, 'r') as file:
        html = file.read()
    return html

def _open_csv_file(filename):
    with open(filename, newline='') as file:
        values = [row[0] for row in csv.reader(file, delimiter=';')]
    return values

def _error_handler(filename, funct):
    if os.path.isfile(filename):
        return funct(filename)
    raise FileNotFoundError(f'File {filename} was not found.')
