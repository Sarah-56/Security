import psutil
import yara
import os
import fnmatch
import time
from termcolor import colored
from pyudev import Context, Monitor
import pyudev

def recursive_scan(dirs, exet):
    files_list = list()
    for (dirpath, dirnames, filenames) in os.walk(dirs):
        files_list += [os.path.join(dirpath, file) for file in fnmatch.filter(filenames, exet)]
    return files_list

def yara_rules_match(yarafolder):
    files = {}
    for x, i in enumerate(recursive_scan(yarafolder, '*.yar')):
        files[str(x)] = str(i)
    return yara.compile(filepaths=files)

def scan(path, yarafolder):
    rules = yara_rules_match(yarafolder)
    if os.path.isfile(path):
        matched = rules.match(path)
        if len(matched) > 0:
            return True
        else:
            return False
    elif os.path.isdir(path):
        listof = recursive_scan(path, '*')
        for i in listof:
            matched = rules.match(i)
            if len(matched) > 0:
                print(colored('[✗] ', 'red'),i)
            else:
                print(colored('[✔] ', 'green'),i)