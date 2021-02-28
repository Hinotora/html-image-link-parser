from bs4 import BeautifulSoup
import json
import re


# Validate JSON
def isJSON(file):
    with open(file, 'r') as file:
        try:
            json.load(file)
        except json.decoder.JSONDecodeError:
            return False
        else:
            return True
    file.close()


# Validate HTML
def isHTML(file):
    with open(file, 'r') as file:
        return bool(BeautifulSoup(file, "html.parser").find())
    file.close()


# Main parse enter point
def parse(file_to_parse, file_to_result):

    print(f'Parsing {file_to_parse}. It may take a few minutes.', end='')

    # Check type of file (JSON or HTML)
    if isHTML(file_to_parse):
        parse_html(file_to_parse, file_to_result)
    elif isJSON(file_to_parse):
        parse_json(file_to_parse, file_to_result)
    else:
        raise Exception('Unknown type of file')


# Html parse function
def parse_html(file_to_parse, file_to_result):

    try:

        rfile = open(f'{file_to_result}/output.txt', 'a+')

        with open(file_to_parse, 'r', encoding="utf-8") as pfile:

            soup = BeautifulSoup(pfile, "html.parser")

            for link in soup.findAll('a'):

                current = link.get('href')

                if re.match(r'(https?:\/\/.*\.(?:png|jpg))', current):
                    rfile.write(current+"\n")

            pfile.close()

        rfile.close()

    except:
        print(' >>> Fail')
        raise
    else:
        print(' >>> Success')


# JSON parse function
def parse_json(file_to_parse, file_to_result):
    # TODO

    try:
        print('>>> JSON parsing not developed yet')
    except:
        print('>>> Fail')
        raise
    else:
        # print('>>> Success')
