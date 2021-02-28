from os import path, mkdir, listdir
from sys import exit
from . import parser, downloader


# Checking path arguments
def check_paths(input_path, output_path):

    # Check input path exist
    if not path.exists(input_path):
        raise Exception('Input file/folder path does not exist.')

    # Check output path exist
    if not path.exists(output_path):
        raise Exception('Output folder does not exist.')

    return (input_path, output_path)


# Starting main parser
def start_parse(input_path, output_path):

    # If input path is file, just parse it
    if path.isfile(input_path):
        parser.parse(input_path, output_path)
    # If input path is folder, parse all files in cycle
    elif path.isdir(input_path):
        for filename in listdir(input_path):
            parser.parse(input_path+'/'+filename, output_path)
    else:
        raise Exception('Unknown type of input path')


# Starting main parser
def start_download(output_path):

    print('\n\n Starting download \n\n')

    # Links are stored in OUTPUT_PATH/output.txt
    links_file = output_path+'/output.txt'

    if not path.exists(links_file) and not path.isfile(links_file):
        raise Exception(f'Can\'t find output.txt in {output_path}')

    # Count number of lines
    links_count = downloader.count(links_file)

    print(f'Total {links_count} to download. Ctrl + C to abort.')

    downloader.download(links_file, output_path, links_count)


# Enter point into script
def init(args):

    input_path = args.INPUT_PATH
    output_path = args.OUTPUT_PATH
    download = args.download

    try:
        input_path, output_path = check_paths(input_path, output_path)

        start_parse(input_path, output_path)

        if download == True:
            start_download(output_path)

    except Exception as e:
        print(f'\n>>>>> Exception: {e} <<<<<\n')
    else:
        print('\n\nCompleted!\n\n')
