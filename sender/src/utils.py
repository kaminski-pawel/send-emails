import csv


def open_html_file(filename):
    with open(filename, 'r') as file:
        html = file.read()
    return html

def open_csv_file(filename):
    with open(filename, newline='') as file:
        values = [row[0] for row in csv.reader(file, delimiter=';')]
    return values