# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class MediaList(ListResource):

    def __init__(self, version, account_sid, message_sid):
        """
        Initialize the MediaList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param message_sid: Contextual message_sid
        
        :returns: MediaList
        :rtype: MediaList
        """
        super(MediaList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'message_sid': message_sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media.json'.format(**self._kwargs)

    def read(self, date_created=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'DateCreated': serialize.iso8601_date(date_created),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            MediaInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, date_created=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'DateCreated': serialize.iso8601_date(date_created),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            MediaInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a MediaContext
        
        :param sid: Contextual sid
        
        :returns: MediaContext
        :rtype: MediaContext
        """
        return MediaContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MediaList>'


class MediaContext(InstanceContext):

    def __init__(self, version, account_sid, message_sid, sid):
        super(MediaContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json'.format(**self._kwargs)

    def delete(self):
        return self._version.delete('delete', self._uri)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            MediaInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )


class MediaInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, message_sid, sid=None):
        super(MediaInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'content_type': payload['content_type'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'parent_sid': payload['parent_sid'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = MediaContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['message_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def content_type(self):
        """ The content_type """
        return self._properties['content_type']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def parent_sid(self):
        """ The parent_sid """
        return self._properties['parent_sid']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def delete(self):
        self._context.delete()

    def fetch(self):
        self._context.fetch()
