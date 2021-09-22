"""
Usage:
    It takes the form of calling each function from the main function at the end of the file.
    All function names are described by default, so please customize by comment operation.
"""

import subprocess
import webbrowser


def auto_browsing():
    """ Enter the url you want to open in the variable urls. The default browser registered on your PC will be launched. """

    urls = (
        'https://translate.google.com/?hl=ja&sl=ja&tl=en&op=translate',
        'https://renso-ruigo.com/',
        'https://github.com/naruhide/en-ja-daily',
        'https://muumuu-mail.com/login',
    )

    for url in urls:
        webbrowser.open(url)


def launch_apps():
    """" Enter the full path of the app you want to launch in the variable app_absolute_paths """

    app_absolute_paths = (
        "/usr/bin/gedit",
    )

    for app in app_absolute_paths:
        subprocess.Popen(app)


def main():
    """ Adjust the function you want to use with comments. """

    auto_browsing()
    # launch_apps()


if __name__ == "__main__":
    main()
    print('Done')
