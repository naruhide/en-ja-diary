#!/usr/bin/env python3
# [summary] ...
"""
Description:
    This file is a collection of functions that help automate routine tasks.
    Each function dares to tolerate code duplication and redundancy to avoid dependencies from other functions.
    Each function is called from the main function at the bottom of the file, so please customize it freely.
"""

import argparse
import os
import subprocess
import webbrowser
from zipfile import is_zipfile
from zipfile import ZipFile

from github import Github


def add_summary_to_readme():
    """
    Purpose:
    Prerequisite:
        echo 'export GIT_ACCESS_TOKEN="your_github_access_token"' >> ~/.bashrc
        Restart bash.
    """

    github_owner_and_repo_name = 'naruhide/en-ja-diary'
    access_token = os.environ['GIT_ACCESS_TOKEN']
    target_dir = 'diaries'

    gh = Github(access_token)
    repo = gh.get_repo(github_owner_and_repo_name)
    contents = repo.get_contents(target_dir)

    # local_num_of_files = len(os.listdir('/home/naruhide/Desktop/en-ja-diary/diaries'))
    # remote_num_of_files = len(contents)
    # if local_num_of_files != remote_num_of_files:
    #     pass
    # else:
    #     pass

    while contents:
        file_content = contents.pop(0)
        print(file_content.path)

    # bytes_content = file_content.decoded_content
    # str_content = bytes_content.decode('utf-8')
    # print(str_content)


def auto_browsing():
    """
    Purpose:
        Open all the usual pages together.
    Usage:
        Enter the url you want to open in the variable urls.
        The default browser registered on your PC will be launched.
    """

    urls = (
        'https://translate.google.com/?hl=ja&sl=ja&tl=en&op=translate',
        'https://renso-ruigo.com/',
        'https://muumuu-mail.com/login',
        'https://github.com/naruhide/en-ja-daily/tree/master/dailys',
        'https://docs.python.org/ja/3/library/index.html',
        'https://wiki.python.org/moin/UsefulModules',
        'https://docs.ansible.com/ansible/2.9_ja/#',
    )

    for url in urls:
        webbrowser.open(url)


def launch_apps():
    """
    Purpose:
        Launch apps in bulk.
    Usage:
        Enter the full path of the app you want to launch in the variable app_absolute_paths.
        If you pass an argument at startup, write it in the tuple with an absolute path as well.
    Example:
        ('/usr/bin/gedit', '/home/testuser/doc/test.txt') # Pass arguments to gedit.
        ('ls', '-la')                                     # Pass options to ls command.
        ls                                                # Tuples are not needed if there are no arguments or options.
    """

    app_absolute_paths = (
        ('/usr/bin/gedit', '/home/naruhide/Desktop/Memos/diary1.txt'),
        '/snap/bin/pycharm-community',
    )

    for app in app_absolute_paths:
        try:
            subprocess.Popen(app)
        except FileNotFoundError as err:
            print(err)
            continue


def unzip():
    """
    Purpose:
        Unzip the zip file to the same hierarchy where you ran this python file.
    Usage:
        Enter the following command on the command line to display the help page.
            python3 python.py -h
    Example:
        python3 python.py --zipfile test1.zip test2.zip
        python3 python.py --zipfile /home/testuser/doc/test1.zip
        python3 python.py --zipfile ~/test1.zip /home/testuser/test2.zip

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
    """ Adjust the function you want to use with comments. """

    add_summary_to_readme()
    # auto_browsing()
    # launch_apps()
    # unzip()


if __name__ == "__main__":
    main()
    print('Done')
