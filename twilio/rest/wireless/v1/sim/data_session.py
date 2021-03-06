# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DataSessionList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sim_sid):
        """
        Initialize the DataSessionList

        :param Version version: Version that contains the resource
        :param sim_sid: The sim_sid

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        """
        super(DataSessionList, self).__init__(version)

        # Path Solution
        self._solution = {'sim_sid': sim_sid}
        self._uri = '/Sims/{sim_sid}/DataSessions'.format(**self._solution)

    def stream(self, end=values.unset, start=values.unset, limit=None,
               page_size=None):
        """
        Streams DataSessionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end: The end
        :param datetime start: The start
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(end=end, start=start, page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, end=values.unset, start=values.unset, limit=None,
             page_size=None):
        """
        Lists DataSessionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end: The end
        :param datetime start: The start
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        return list(self.stream(end=end, start=start, limit=limit, page_size=page_size))

    def page(self, end=values.unset, start=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DataSessionInstance records from the API.
        Request is executed immediately

        :param datetime end: The end
        :param datetime start: The start
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        params = values.of({
            'End': serialize.iso8601_datetime(end),
            'Start': serialize.iso8601_datetime(start),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DataSessionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DataSessionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DataSessionPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.DataSessionList>'


class DataSessionPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the DataSessionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param sim_sid: The sim_sid

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        super(DataSessionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DataSessionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        """
        return DataSessionInstance(self._version, payload, sim_sid=self._solution['sim_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.DataSessionPage>'


class DataSessionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, sim_sid):
        """
        Initialize the DataSessionInstance

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        """
        super(DataSessionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'sim_sid': payload['sim_sid'],
            'account_sid': payload['account_sid'],
            'radio_link': payload['radio_link'],
            'operator_mcc': deserialize.integer(payload['operator_mcc']),
            'operator_mnc': deserialize.integer(payload['operator_mnc']),
            'operator_country': payload['operator_country'],
            'operator_name': payload['operator_name'],
            'cell_id': payload['cell_id'],
            'cell_location_estimate': payload['cell_location_estimate'],
            'packets_uploaded': deserialize.integer(payload['packets_uploaded']),
            'packets_downloaded': deserialize.integer(payload['packets_downloaded']),
            'last_updated': deserialize.iso8601_datetime(payload['last_updated']),
            'start': deserialize.iso8601_datetime(payload['start']),
            'end': deserialize.iso8601_datetime(payload['end']),
        }

        # Context
        self._context = None
        self._solution = {'sim_sid': sim_sid}

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sim_sid(self):
        """
        :returns: The sim_sid
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def radio_link(self):
        """
        :returns: The radio_link
        :rtype: unicode
        """
        return self._properties['radio_link']

    @property
    def operator_mcc(self):
        """
        :returns: The operator_mcc
        :rtype: unicode
        """
        return self._properties['operator_mcc']

    @property
    def operator_mnc(self):
        """
        :returns: The operator_mnc
        :rtype: unicode
        """
        return self._properties['operator_mnc']

    @property
    def operator_country(self):
        """
        :returns: The operator_country
        :rtype: unicode
        """
        return self._properties['operator_country']

    @property
    def operator_name(self):
        """
        :returns: The operator_name
        :rtype: unicode
        """
        return self._properties['operator_name']

    @property
    def cell_id(self):
        """
        :returns: The cell_id
        :rtype: unicode
        """
        return self._properties['cell_id']

    @property
    def cell_location_estimate(self):
        """
        :returns: The cell_location_estimate
        :rtype: dict
        """
        return self._properties['cell_location_estimate']

    @property
    def packets_uploaded(self):
        """
        :returns: The packets_uploaded
        :rtype: unicode
        """
        return self._properties['packets_uploaded']

    @property
    def packets_downloaded(self):
        """
        :returns: The packets_downloaded
        :rtype: unicode
        """
        return self._properties['packets_downloaded']

    @property
    def last_updated(self):
        """
        :returns: The last_updated
        :rtype: datetime
        """
        return self._properties['last_updated']

    @property
    def start(self):
        """
        :returns: The start
        :rtype: datetime
        """
        return self._properties['start']

    @property
    def end(self):
        """
        :returns: The end
        :rtype: datetime
        """
        return self._properties['end']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.DataSessionInstance>'
