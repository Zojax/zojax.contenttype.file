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
""" page interfaces

$Id$
"""
import string

from zope import interface, component
from zope.schema.fieldproperty import FieldProperty
from zope.size import byteDisplay
from zope.size.interfaces import ISized
#from zope.app.container.contained import NameChooser

from zojax.content.type.item import PersistentItem
from zojax.content.type.contenttype import ContentType
from zojax.filefield.field import FileFieldProperty
#from zojax.filefield.interfaces import IFile as IFileData

from interfaces import IFile


class File(PersistentItem):
    interface.implements(IFile)

    data = FileFieldProperty(IFile['data'])

    disposition = FieldProperty(IFile['disposition'])

    accessMode = FieldProperty(IFile['accessMode'])

    @property
    def canDownload(self):
        return self.accessMode in ['all', 'download'] and self.data.size

    @property
    def canPreview(self):
        return self.accessMode in ['all', 'preview'] and \
            self.data.previewIsAvailable


class Sized(object):
    component.adapts(IFile)
    interface.implements(ISized)

    def __init__(self, context):
        self.context = context

    def sizeForSorting(self):
        return "byte", self.context.data.size

    def sizeForDisplay(self):
        return byteDisplay(self.context.data.size)


class FileType(ContentType):

    def add(self, content, name=''):
        if not name and content is not None:
            try:
                name = content.data.filename.split('\\')[-1].split('/')[-1].lower()
                valid_chars = "-.%s%s" % (string.lowercase, string.digits)
                name = ''.join(c for c in name if c in valid_chars)
            except AttributeError:
                pass
        return super(FileType, self).add(content, name)
