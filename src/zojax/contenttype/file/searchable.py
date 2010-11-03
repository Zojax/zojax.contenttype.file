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
""" ISearchableText for ISO

$Id$
"""
from zopyx.txng3.core.interfaces.converter import IConverter
from zope.component.interfaces import ComponentLookupError
from zope import interface, component
from zope.index.text.interfaces import ISearchableText

from zojax.content.type.searchable import ContentSearchableText

from interfaces import IFile


class FileSearchableText(ContentSearchableText):
    """search text
    """
    component.adapts(IFile)
    interface.implements(ISearchableText)

    def __init__(self, content):
        self.content = content

    def getSearchableText(self):
        res = super(FileSearchableText, self).getSearchableText()
        try:
            converter = component.getUtility(IConverter, self.content.data.mimeType)
            if converter.isAvailable():
                res += ' ' + unicode(*converter.convert(self.content.data.data, 'utf-8', 'text/plain'))
        except ComponentLookupError:
            pass
        return res
        