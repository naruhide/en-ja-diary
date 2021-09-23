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
from zipfile import is_zipfile
from zipfile import ZipFile


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
        '/snap/bin/pycharm-communit',
    )

    for app in app_absolute_paths:
        try:
            subprocess.Popen(app)
        except FileNotFoundError as err:
            print(err)
            continue


def unzip():
    """
    Unzip the zip file to the same hierarchy where you ran this python file.
    The function to unzip the password-protected zip file has not been implemented yet.

    Example:
        python3 python.py --zipfile test1.zip test2.zip
        python3 python.py --zipfile /home/testuser/doc/test1.zip
        python3 python.py --zipfile ~/test1.zip /home/testuser/test2.zip

    Enter the following command on the command line to display the help page.
        python3 python.py -h
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
        if is_zipfile(file):
            with ZipFile(file) as zf:
                zf.extractall()
        else:
            print(f'{file} is not zip file format.')
            continue


def main():
    """Adjust the function you want to use with comments."""

    # auto_browsing()
    # launch_apps()
    # unzip()


if __name__ == "__main__":
    main()
    print('Done')
