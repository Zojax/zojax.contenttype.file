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
from zojax.statusmessage.interfaces import IStatusMessage


class FileDownload(object):

    def show(self):
        if self.context.canDownload:
            try:
                filename = self.context.data.filename
            except:
                filename = self.context.__name__

            return self.context.data.show(
                self.request,
                filename=filename,
                contentDisposition=self.context.disposition)


class FilePreview(object):

    def show(self):
        if self.context.canPreview:
            try:
                filename = self.context.data.filename
            except:
                filename = self.context.__name__

            return self.context.data.showPreview(
                self.request,
                filename=filename,
                contentDisposition='inline')


class FileView(object):

    def size(self):
        return ISized(self.context).sizeForDisplay()


class FileDownloadView(object):

    def filename(self):
        # import pdb; pdb.set_trace()
        file_url = '/'.join(self.request.URL.__str__().split('/')[:-1])
        if self.context.data.size > 0:
            self.redirect(file_url+'/download.html')
        else:
            IStatusMessage(self.request).add('File no longer exists or has been deleted')
        try:
            filename = self.context.data.filename
        except:
            filename = self.context.__name__

        return filename


class FilePreviewView(object):

    def filename(self):
        try:
            filename = self.context.data.filename
        except:
            filename = self.context.__name__

        return filename


class FileViewView(object):
    interface.implements(IContentViewView)
    component.adapts(IFile, interface.Interface)

    name = u'index.html'

    def __init__(self, file, request):
        pass
