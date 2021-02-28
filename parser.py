import argparse
from html_image_link_parser import core


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT_PATH', type=str, help='Input file/folder path')
    parser.add_argument('OUTPUT_PATH', type=str, help='Output folder path')
    parser.add_argument('--download', action="store_const",
                        const=True, help='Parse and download images in the same folder')
    args = parser.parse_args()

    core.init(args)
