# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class ParticipantList(ListResource):

    def __init__(self, version, conversation_sid):
        """
        Initialize the ParticipantList
        
        :param Version version: Version that contains the resource
        :param conversation_sid: Contextual conversation_sid
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        super(ParticipantList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'conversation_sid': conversation_sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Participants'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, to, from_):
        data = values.of({
            'To': to,
            'From': from_,
        })
        
        return self._version.create(
            ParticipantInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: Contextual sid
        
        :returns: ParticipantContext
        :rtype: ParticipantContext
        """
        return ParticipantContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantList>'


class ParticipantContext(InstanceContext):

    def __init__(self, version, conversation_sid, sid):
        super(ParticipantContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'conversation_sid': conversation_sid,
            'sid': sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Participants/{sid}'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )


class ParticipantInstance(InstanceResource):

    def __init__(self, version, payload, conversation_sid, sid=None):
        super(ParticipantInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'address': payload['address'],
            'status': payload['status'],
            'conversation_sid': payload['conversation_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'duration': payload['duration'],
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'conversation_sid': conversation_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ParticipantContext(
                self._version,
                self._context_properties['conversation_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def address(self):
        """ The address """
        return self._properties['address']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def conversation_sid(self):
        """ The conversation_sid """
        return self._properties['conversation_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def start_time(self):
        """ The start_time """
        return self._properties['start_time']

    @property
    def end_time(self):
        """ The end_time """
        return self._properties['end_time']

    @property
    def duration(self):
        """ The duration """
        return self._properties['duration']

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    def fetch(self):
        self._context.fetch()
