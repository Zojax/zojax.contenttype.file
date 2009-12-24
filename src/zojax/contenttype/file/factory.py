##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""File factory for zope.filerepresentation

$Id$
"""
from zope.component import adapts
from zope.event import notify
from zope.filerepresentation.interfaces import IFileFactory
from zope.interface import implements, Interface
from zope.lifecycleevent import ObjectCreatedEvent
from zojax.filefield.data import FileData

from zojax.contenttype.file.file import File


class FileFactory(object):
    
    adapts(Interface)
    implements(IFileFactory)
    
    def __init__(self, context):
        self.context = context
    
    def __call__(self, name, content_type, data):
        file = File()
        notify(ObjectCreatedEvent(file))
        file.title = name
        file.data = FileData(data, name)
        return file
