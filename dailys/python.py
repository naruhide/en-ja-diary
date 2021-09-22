"""


"""

import os.path
import sys
import subprocess
import webbrowser

def auto_app():
    dirname = os.path.dirname(__file__)
    app_file = os.path.join(dirname, "config", "app.txt")  # appfile is here.
    try:
        with open(app_file, "r", encoding="utf8") as f:
            path_with_line_breaks = f.readlines()
            app_paths = list(map(lambda s: s.rstrip("\n"), path_with_line_breaks))
        for app in app_paths:
            subprocess.Popen(app)
    except FileNotFoundError as err:
        print(err)
        sys.exit()

def browser():
    dirname = os.path.dirname(__file__)
    url_file = os.path.join(dirname, "config", "url.txt")  # urlfile is here.
    try:
        with open(url_file, "r", encoding="utf8") as f:
            urls_with_line_breaks = f.readlines()
            urls = list(map(lambda s: s.rstrip("\n"), urls_with_line_breaks))
    except FileNotFoundError as err:
        print(err)
        sys.exit()

    for url in urls:
        webbrowser.open(url)

if '__name__' == '__main__':
    auto_app()
    browser()