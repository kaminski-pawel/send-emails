
def open_html_file(filename):
    with open(filename, 'r') as file:
        html = file.read()
    return html