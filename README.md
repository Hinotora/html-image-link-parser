## Simple HTML image url parser

Initially I developed it for myself, since I had to extract a huge number of links to pictures from an HTML document.

## Description

Script extracts from documents all <a> tags, and checks if this link is a link to a picture, then this link is saved to file `output.txt`. Also it can download all these pictures after parsing.

## Installation

Clone repo:

```bash
$ git clone https://github.com/Hinotora/html-image-link-parser.git
```

Install packages via pip (also you can create virtualenv):
```bash
$ cd html-image-link-parser
$ pip install -r requirements.txt
```

## Usage

```python
$ python3 parser.py FILE_OR_FOLDER PATH_TO_RESULT_FOLDER [--download]
```

`FILE_OR_FOLDER` - Folder contains html documents OR path to single document.

`PATH_TO_RESULT_FOLDER` - Folder contains `output.txt` with links extracted from documents and downloaded images (with `--downlaoded` option).

`--download` - Script will download parsed links into `PATH_TO_RESULT_FOLDER` images will have `.jpg` format.

An example, we will parse all files in `/home/user/files_to_parse` and results will be in `/home/user/results`, so command will look like:

```python
# Parse all files in folder
$ python3 parser.py ~/files_to_parse ~/results

# Parse single file
$ python3 parser.py ~/files_to_parse/doc.html ~/results

# Parse with download into ~/results
$ python3 parser.py ~/files_to_parse ~/results --download
```
## Contributing
Pull requests are welcome.

## License
Do what you want, but leave the link to this repo
