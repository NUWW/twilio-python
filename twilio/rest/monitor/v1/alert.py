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


class AlertList(ListResource):

    def __init__(self, version):
        """
        Initialize the AlertList
        
        :param Version version: Version that contains the resource
        
        :returns: AlertList
        :rtype: AlertList
        """
        super(AlertList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Alerts'.format(**self._kwargs)

    def read(self, log_level=values.unset, start_date=values.unset,
             end_date=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'LogLevel': log_level,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            AlertInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, log_level=values.unset, start_date=values.unset,
             end_date=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'LogLevel': log_level,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AlertInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a AlertContext
        
        :param sid: Contextual sid
        
        :returns: AlertContext
        :rtype: AlertContext
        """
        return AlertContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor.V1.AlertList>'


class AlertContext(InstanceContext):

    def __init__(self, version, sid):
        super(AlertContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Alerts/{sid}'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AlertInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)


class AlertInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        super(AlertInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'alert_text': payload['alert_text'],
            'api_version': payload['api_version'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_generated': deserialize.iso8601_datetime(payload['date_generated']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'error_code': payload['error_code'],
            'log_level': payload['log_level'],
            'more_info': payload['more_info'],
            'request_method': payload['request_method'],
            'request_url': payload['request_url'],
            'request_variables': payload['request_variables'],
            'resource_sid': payload['resource_sid'],
            'response_body': payload['response_body'],
            'response_headers': payload['response_headers'],
            'sid': payload['sid'],
            'url': payload['url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = AlertContext(
                self._version,
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def alert_text(self):
        """ The alert_text """
        return self._properties['alert_text']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_generated(self):
        """ The date_generated """
        return self._properties['date_generated']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def error_code(self):
        """ The error_code """
        return self._properties['error_code']

    @property
    def log_level(self):
        """ The log_level """
        return self._properties['log_level']

    @property
    def more_info(self):
        """ The more_info """
        return self._properties['more_info']

    @property
    def request_method(self):
        """ The request_method """
        return self._properties['request_method']

    @property
    def request_url(self):
        """ The request_url """
        return self._properties['request_url']

    @property
    def request_variables(self):
        """ The request_variables """
        return self._properties['request_variables']

    @property
    def resource_sid(self):
        """ The resource_sid """
        return self._properties['resource_sid']

    @property
    def response_body(self):
        """ The response_body """
        return self._properties['response_body']

    @property
    def response_headers(self):
        """ The response_headers """
        return self._properties['response_headers']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
