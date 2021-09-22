# python.py
#!/usr/bin/env python3
"""
Usage:
    It takes the form of calling each function from the main function at the end of the file.
    All function names are described by default, so please customize by comment operation.
"""

import subprocess
import sys
import webbrowser


def auto_browsing():
    """
    Enter the url you want to open in the variable urls.
    The default browser registered on your PC will be launched.
    """

    urls = (
        'https://translate.google.com/?hl=ja&sl=ja&tl=en&op=translate',
        'https://renso-ruigo.com/',
        'https://github.com/naruhide/en-ja-daily',
        'https://muumuu-mail.com/login',
        'https://docs.python.org/3/library/index.html',
    )

    for url in urls:
        webbrowser.open(url)


def launch_apps():
    """
    Enter the full path of the app you want to launch in the variable app_absolute_paths
    If you pass an argument at startup, write it in the tuple with an absolute path as well.
    """

    app_absolute_paths = (
        ('/usr/bin/gedit', '/home/naruhide/Desktop/Memos/diary1.txt'),
        ('ls', '-l'),
        'ls',
    )

    try:
        for app in app_absolute_paths:
            subprocess.Popen(app)
    except FileNotFoundError as err:
        print(err)
        sys.exit()


def main():
    """Adjust the function you want to use with comments."""

    auto_browsing()
    # launch_apps()


if __name__ == "__main__":
    main()
    print('Done')
