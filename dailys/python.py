"""


"""

import os.path
import subprocess
import sys
import webbrowser


def auto_browser():
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


def launch_app():
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


def main():
    """ Please adjust the function you want to use with comments. """

    # auto_browse()
    # launch_app()

    print('Done')


if __name__ == "__main__":
    main()