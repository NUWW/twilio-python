# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class StatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid, workflow_sid):
        super(StatisticsContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'workflow_sid': workflow_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics'.format(**self._kwargs)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        params = values.of({
            'Minutes': minutes,
            'StartDate': start_date,
            'EndDate': end_date,
        })
        
        return self._version.fetch(
            StatisticsInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )


class StatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid=None, workflow_sid=None):
        super(StatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'workflow_sid': payload['workflow_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],
            'workflow_sid': workflow_sid or self._properties['workflow_sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = StatisticsContext(
                self._version,
                self._context_properties['workspace_sid'],
                self._context_properties['workflow_sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """ The cumulative """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """ The realtime """
        return self._properties['realtime']

    @property
    def workflow_sid(self):
        """ The workflow_sid """
        return self._properties['workflow_sid']

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._properties['workspace_sid']

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset):
        self._context.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
        )
