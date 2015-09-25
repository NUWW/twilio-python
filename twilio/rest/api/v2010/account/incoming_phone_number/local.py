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


class LocalList(ListResource):

    def __init__(self, version, owner_account_sid):
        """
        Initialize the LocalList
        
        :param Version version: Version that contains the resource
        :param owner_account_sid: Contextual owner_account_sid
        
        :returns: LocalList
        :rtype: LocalList
        """
        super(LocalList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
        }
        self._uri = '/Accounts/{owner_account_sid}/IncomingPhoneNumbers/Local.json'.format(**self._kwargs)

    def read(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            LocalInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            LocalInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, area_code, phone_number, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset):
        data = values.of({
            'AreaCode': area_code,
            'PhoneNumber': phone_number,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        
        return self._version.create(
            LocalInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a LocalContext
        
        :param sid: Contextual sid
        
        :returns: LocalContext
        :rtype: LocalContext
        """
        return LocalContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LocalList>'


class LocalContext(InstanceContext):

    def __init__(self, version, owner_account_sid, sid):
        super(LocalContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'owner_account_sid': owner_account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{owner_account_sid}/IncomingPhoneNumbers/{sid}.json'.format(**self._kwargs)


class LocalInstance(InstanceResource):

    def __init__(self, version, payload, owner_account_sid, sid=None):
        super(LocalInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'address_requirements': payload['address_requirements'],
            'api_version': payload['api_version'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'sid': payload['sid'],
            'sms_application_sid': payload['sms_application_sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'uri': payload['uri'],
            'voice_application_sid': payload['voice_application_sid'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'owner_account_sid': owner_account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = LocalContext(
                self._version,
                self._context_properties['owner_account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def address_requirements(self):
        """ The address_requirements """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def beta(self):
        """ The beta """
        return self._properties['beta']

    @property
    def capabilities(self):
        """ The capabilities """
        return self._properties['capabilities']

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
    def phone_number(self):
        """ The phone_number """
        return self._properties['phone_number']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """ The sms_application_sid """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """ The sms_fallback_method """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """ The sms_fallback_url """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """ The sms_method """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """ The sms_url """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """ The status_callback """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """ The status_callback_method """
        return self._properties['status_callback_method']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    @property
    def voice_application_sid(self):
        """ The voice_application_sid """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """ The voice_caller_id_lookup """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """ The voice_fallback_method """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """ The voice_fallback_url """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """ The voice_method """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """ The voice_url """
        return self._properties['voice_url']
