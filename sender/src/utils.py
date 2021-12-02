import csv
import json


def open_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def open_html_file(filename):
    with open(filename, 'r') as file:
        html = file.read()
    return html

def open_csv_file(filename):
    with open(filename, newline='') as file:
        values = [row[0] for row in csv.reader(file, delimiter=';')]
    return values