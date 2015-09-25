# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address import IpAddressList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class IpAccessControlListList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the IpAccessControlListList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: IpAccessControlListList
        :rtype: IpAccessControlListList
        """
        super(IpAccessControlListList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists.json'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            IpAccessControlListInstance,
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
            IpAccessControlListInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name):
        data = values.of({
            'FriendlyName': friendly_name,
        })
        
        return self._version.create(
            IpAccessControlListInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a IpAccessControlListContext
        
        :param sid: Contextual sid
        
        :returns: IpAccessControlListContext
        :rtype: IpAccessControlListContext
        """
        return IpAccessControlListContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAccessControlListList>'


class IpAccessControlListContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(IpAccessControlListContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._ip_addresses = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            IpAccessControlListInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name):
        data = values.of({
            'FriendlyName': friendly_name,
        })
        
        return self._version.update(
            IpAccessControlListInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    @property
    def ip_addresses(self):
        if self._ip_addresses is None:
            self._ip_addresses = IpAddressList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                ip_access_control_list_sid=self._kwargs['sid'],
            )
        return self._ip_addresses


class IpAccessControlListInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(IpAccessControlListInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'subresource_uris': payload['subresource_uris'],
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
            self._lazy_context = IpAccessControlListContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name):
        self._context.update(
            friendly_name,
        )

    def delete(self):
        self._context.delete()

    @property
    def ip_addresses(self):
        return self._context.ip_addresses
