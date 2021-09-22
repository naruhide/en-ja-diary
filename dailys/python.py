"""


"""

import subprocess
import webbrowser


def auto_browsing():
    """
    Enter the url you want to open in the variable urls.
    The default browser registered on your PC will be launched.
    """

    urls = (
        'https://github.com/naruhide/my-util',
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
