import requests
import time


# Generate blocks for more perform line counting
def blocks(files, size=65536):
    try:
        while True:
            b = files.read(size)
            if not b:
                break
            yield b
    except:
        raise


# Count number of links in file
def count(links_file):
    try:
        with open(links_file, "r", encoding="utf-8", errors='ignore') as f:
            return sum(bl.count("\n") for bl in blocks(f))
    except:
        raise


# Start downlaoding
def download(links_file, output_path, count):

    try:
        with open(links_file, 'r') as file:

            links = file.readlines()

            downloaded = 1

            for link in links:
                print(f"[{downloaded}/{count}] downloading: {link[:-1]}", end='')

                response = requests.get(link)

                image = open(f"{output_path}/{downloaded}.jpg", "wb")

                if bool(image.write(response.content)):
                    print(" >>> Success")
                else:
                    print(" >>> Fail")

                image.close()

                downloaded += 1

                time.sleep(0.3)

        file.close()
    except:
        raise
