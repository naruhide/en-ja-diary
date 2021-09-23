#!/usr/bin/env python3
# python.py
"""
Usage:
    It takes the form of calling each function from the main function at the end of the file.
    In the main function, all function names are described by default, so please customize by comment operation.
"""

import argparse
import subprocess
import webbrowser
import zipfile


def auto_browsing():
    """
    Enter the url you want to open in the variable urls.
    The default browser registered on your PC will be launched.
    """

    urls = (
        'https://translate.google.com/?hl=ja&sl=ja&tl=en&op=translate',
        'https://renso-ruigo.com/',
        'https://github.com/naruhide/en-ja-daily/tree/master/dailys',
        'https://muumuu-mail.com/login',
        'https://docs.python.org/ja/3/library/index.html',
        'https://docs.ansible.com/ansible/2.9_ja/#',
    )

    for url in urls:
        webbrowser.open(url)


def launch_apps():
    """
    Enter the full path of the app you want to launch in the variable app_absolute_paths
    If you pass an argument at startup, write it in the tuple with an absolute path as well.

    Example:
        ('/usr/bin/gedit', '/home/testuser/doc/test.txt')
        ('ls', '-la')
        ls
    """

    app_absolute_paths = (
        ('/usr/bin/gedit', '/home/naruhide/Desktop/Memos/diary1.txt'),
        '/snap/bin/pycharm-community',
    )

    try:
        for app in app_absolute_paths:
            subprocess.Popen(app)
    except FileNotFoundError as err:
        print(err)
        return


def unzip():
    """
    Unzip the zip file to the same hierarchy where you ran the python file.
    The function to unzip the password-protected zip file has not been implemented yet.
    """
    # TODO: Function addition
    # Measures against garbled characters.
    # Decompression of password-protected files and multi-support.

    parser = argparse.ArgumentParser()
    parser.add_argument('--zipfile', nargs='*',
                        help='Absolute or relative path of the zip file you want to unzip. Multiple is possible.')
    # parser.add_argument('--password', nargs='*',
    #                     help='Password set in the zip file. If you use this option, limit the zipfile option to one.')
    args = parser.parse_args()
    zipfile_list = args.zipfile
    # password_list = args.password

    if zipfile_list is None:
        return
    for file in zipfile_list:
        if zipfile.is_zipfile(file):
            with zipfile.ZipFile(file) as zf:
                zf.extractall()
        else:
            print(f'{file} is not zip file format.')
            return


def main():
    """Adjust the function you want to use with comments."""

    # auto_browsing()
    # launch_apps()
    unzip()


if __name__ == "__main__":
    main()
    print('Done')
