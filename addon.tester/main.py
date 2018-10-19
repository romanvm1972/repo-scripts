# coding: utf-8

import sys
from pprint import pformat
import xbmc
import xbmcgui
import web_pdb

class User(xbmcgui.ListItem):
    def __new__(cls, name, label2="", iconImage="", thumbnailImage="", path="", window=None, userdata=None):
        return super(User, cls).__new__(cls, name, label2="", iconImage="", thumbnailImage="", path="")

    def __init__(self, name, label2="", iconImage="", thumbnailImage="", path="", window=None, userdata=None):
        super(User, self).__init__(label=name, label2="", iconImage="", thumbnailImage="", path="")
        self.Base = window
        self.Name = name
        self.UserData = userdata

with web_pdb.catch_post_mortem():
    us = User('foo', window = None, userdata='foo')

web_pdb.set_trace()
