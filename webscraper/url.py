import requests
import re


def extract_urls(string):
    response = requests.get(string)
    html_content = response.text
    url_pattern = 'https?:\/\/[^\s]+?\.(?:jpg|jpeg|png|gif)'

    urls = re.findall(url_pattern, html_content)

    return urls


def main():
    url = "https://www.ucll.be"
    urls = extract_urls(url)

    for url in urls:
        print(url)


main()
