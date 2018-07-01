import sys
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def fetch_live_html(url):
    return AppURLopener().open(url).read()


def write_html_to_file(html, file):
    html_file = open(file, 'w')
    html_file.write(str(html))


def load_test_html(file):
    html_file = open(file, 'r')
    return html_file.read()


def get_html(url, save=False):
    if len(sys.argv) > 1 and sys.argv[1] == 'live':
        html = fetch_live_html(url)
        if save:
            write_html_to_file(html, 'test.html')
        return html
    else:
        print("Using Cached Menu")
        return load_test_html('test.html')

