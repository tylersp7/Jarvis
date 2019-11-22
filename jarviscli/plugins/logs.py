import datetime

from os import system
from colorama import Fore
from plugin import plugin, require


@require(native='grep')
@plugin('logs')
def logs(jarvis, string):
    """
    Matches a string pattern in a file using regex.
    Type "match" and you'll be prompted.
    """
    #file_name = jarvis.input("Enter file name?:\n", Fore.RED)
    pattern = jarvis.input("Enter string:\n", Fore.GREEN)
    file_name = "~/Logs/"+datetime.date.today().strftime('%Y-%m-%d') + ".log"
    system("grep -A1 '" + pattern + "' " + file_name)
