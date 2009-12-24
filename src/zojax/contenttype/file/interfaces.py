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
""" file interfaces

$Id$
"""
from zope import schema, interface
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from zojax.filefield.field import FileField
from zojax.widget.radio.field import RadioChoice
from zojax.contenttypes.interfaces import _

dispositionVocabulary = SimpleVocabulary((
        SimpleTerm('attachment', 'attachment', _('Download')),
        SimpleTerm('inline', 'inline', _('View inline'))))


class IFile(interface.Interface):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'File title.'),
        required = False)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'A short summary of the file.'),
        required = False)

    data = FileField(
        title=_(u'Data'),
        description=_(u'The actual content of the file.'),
        required = False)

    disposition = RadioChoice(
        title = _(u'How do you want to view this file.'),
        vocabulary = dispositionVocabulary,
        default = 'inline',
        required = True)


class IFileType(interface.Interface):
    """ file content type """
