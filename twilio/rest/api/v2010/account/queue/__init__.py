# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.queue.member import MemberList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class QueueList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the QueueList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: QueueList
        :rtype: QueueList
        """
        super(QueueList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues.json'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            QueueInstance,
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
            QueueInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name=values.unset, max_size=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })
        
        return self._version.create(
            QueueInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a QueueContext
        
        :param sid: Contextual sid
        
        :returns: QueueContext
        :rtype: QueueContext
        """
        return QueueContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.QueueList>'


class QueueContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(QueueContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._members = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            QueueInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset, max_size=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })
        
        return self._version.update(
            QueueInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    @property
    def members(self):
        if self._members is None:
            self._members = MemberList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                queue_sid=self._kwargs['sid'],
            )
        return self._members


class QueueInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(QueueInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'average_wait_time': payload['average_wait_time'],
            'current_size': payload['current_size'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'max_size': payload['max_size'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = QueueContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def average_wait_time(self):
        """ The average_wait_time """
        return self._properties['average_wait_time']

    @property
    def current_size(self):
        """ The current_size """
        return self._properties['current_size']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def max_size(self):
        """ The max_size """
        return self._properties['max_size']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, max_size=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            max_size=max_size,
        )

    def delete(self):
        self._context.delete()

    @property
    def members(self):
        return self._context.members
