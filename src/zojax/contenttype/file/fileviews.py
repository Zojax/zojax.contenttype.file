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
"""

$Id$
"""
from zope import interface, component
from zope.size.interfaces import ISized
from zojax.content.type.interfaces import IContentViewView
from zojax.contenttype.file.interfaces import IFile


class FileDownload(object):

    def show(self):
        if self.context.canDownload:
            return self.context.data.show(
                self.request,
                filename=self.context.__name__,
                contentDisposition=self.context.disposition)


class FilePreview(object):

    def show(self):
        if self.context.canPreview:
            return self.context.data.showPreview(
                self.request,
                filename=self.context.__name__,
                contentDisposition='inline')


class FileView(object):

    def size(self):
        return ISized(self.context).sizeForDisplay()


class FileViewView(object):
    interface.implements(IContentViewView)
    component.adapts(IFile, interface.Interface)

    name = u'index.html'

    def __init__(self, file, request):
        pass
