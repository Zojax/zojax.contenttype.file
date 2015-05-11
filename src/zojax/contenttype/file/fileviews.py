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
from zope.proxy import removeAllProxies
from zope.size.interfaces import ISized
# from zope.traversing.browser import absoluteURL

from zojax.content.type.interfaces import IContentViewView
from zojax.contenttype.file.interfaces import IFile
from zojax.contenttypes.interfaces import _
from zojax.statusmessage.interfaces import IStatusMessage


class FileDownload(object):

    def show(self):
        if self.context.canDownload:
            context = removeAllProxies(self.context)
            try:
                filename = context.data.filename
            except:
                filename = context.__name__

            return context.data.show(
                self.request,
                filename=filename,
                contentDisposition=self.context.disposition)

        # NOTE: workaround for the items without a file (#460)
        if not hasattr(self.context.data, 'size') or \
           self.context.data.size == 0:
            IStatusMessage(self.request).add(_(
                'File no longer exists or has been deleted.'))

            self.request.response.redirect('index.html')
            # self.redirect("%s/" % absoluteURL(self.context, self.request))


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


class BaseView(object):

    def filename(self):
        try:
            filename = self.context.data.filename
        except:
            filename = self.context.__name__

        return filename

    def file_exists(self):
        """ checks whether the file exist """

        context = removeAllProxies(self.context)

        if hasattr(context, 'data'):
            if hasattr(context.data, 'size') and context.data.size > 0:
                return True

        IStatusMessage(self.request).add(
            _('File no longer exists or has been deleted.'))
        return False


class FileView(BaseView):

    def size(self):
        return ISized(self.context).sizeForDisplay()


# class FileDownloadView(BaseView):
#
#    def filename(self):
#        context = removeAllProxies(self.context)
#        file_url = '/'.join(self.request.URL.__str__().split('/')[:-1])
#        if self.file_exists():
#            self.redirect(file_url + '/download.html')
#
#        try:
#            filename = self.context.data.filename
#        except:
#            filename = self.context.__name__
#
#        return filename


class FilePreviewView(BaseView):
    """ FilePreview View """


class FileViewView(object):
    interface.implements(IContentViewView)
    component.adapts(IFile, interface.Interface)

    name = u'index.html'

    def __init__(self, file, request):
        pass
