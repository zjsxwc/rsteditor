#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import os.path

from wx import GetTranslation as _

APPNAME = 'RSTEditor'
VERSION = '1.0.0a'
AUTHORS =['Yugang LIU',]

HOME_PATH = os.path.expanduser('~')
BASE_PATH = os.path.join(HOME_PATH, '.config', APPNAME.lower())
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template')

STYLE_FILE = 'styles.ini'
CONFIG_FILE = 'config.ini'

FILENAME = 'Unknown.rst'
ALLOWED_LOADS = ['.rst', '.rest',
        '.html', '.htm',
        '.txt',
        '.c', '.cpp', '.h',
        '.sh',
        '.py']

DATA_PATH = os.path.join('%s/share/%s'% (sys.prefix, APPNAME.lower()))

try:
    import configparser
except:
    import ConfigParser as configparser

config = configparser.ConfigParser()

