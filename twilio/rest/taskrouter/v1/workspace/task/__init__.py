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
from twilio.rest.taskrouter.v1.workspace.task.reservation import ReservationList


class TaskList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the TaskList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: Contextual workspace_sid
        
        :returns: TaskList
        :rtype: TaskList
        """
        super(TaskList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks'.format(**self._kwargs)

    def read(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'Priority': priority,
            'AssignmentStatus': assignment_status,
            'WorkflowSid': workflow_sid,
            'WorkflowName': workflow_name,
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TaskInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset,
             page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'Priority': priority,
            'AssignmentStatus': assignment_status,
            'WorkflowSid': workflow_sid,
            'WorkflowName': workflow_name,
            'TaskQueueSid': task_queue_sid,
            'TaskQueueName': task_queue_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            TaskInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, attributes, workflow_sid, timeout=values.unset,
               priority=values.unset):
        data = values.of({
            'Attributes': attributes,
            'WorkflowSid': workflow_sid,
            'Timeout': timeout,
            'Priority': priority,
        })
        
        return self._version.create(
            TaskInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a TaskContext
        
        :param sid: Contextual sid
        
        :returns: TaskContext
        :rtype: TaskContext
        """
        return TaskContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskList>'


class TaskContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        super(TaskContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._reservations = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TaskInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset):
        data = values.of({
            'Attributes': attributes,
            'AssignmentStatus': assignment_status,
            'Reason': reason,
            'Priority': priority,
        })
        
        return self._version.update(
            TaskInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    @property
    def reservations(self):
        if self._reservations is None:
            self._reservations = ReservationList(
                self._version,
                workspace_sid=self._kwargs['workspace_sid'],
                task_sid=self._kwargs['sid'],
            )
        return self._reservations


class TaskInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        super(TaskInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'age': payload['age'],
            'assignment_status': payload['assignment_status'],
            'attributes': payload['attributes'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'priority': payload['priority'],
            'reason': payload['reason'],
            'sid': payload['sid'],
            'task_queue_sid': payload['task_queue_sid'],
            'timeout': payload['timeout'],
            'workflow_sid': payload['workflow_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TaskContext(
                self._version,
                self._context_properties['workspace_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def age(self):
        """ The age """
        return self._properties['age']

    @property
    def assignment_status(self):
        """ The assignment_status """
        return self._properties['assignment_status']

    @property
    def attributes(self):
        """ The attributes """
        return self._properties['attributes']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def priority(self):
        """ The priority """
        return self._properties['priority']

    @property
    def reason(self):
        """ The reason """
        return self._properties['reason']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def task_queue_sid(self):
        """ The task_queue_sid """
        return self._properties['task_queue_sid']

    @property
    def timeout(self):
        """ The timeout """
        return self._properties['timeout']

    @property
    def workflow_sid(self):
        """ The workflow_sid """
        return self._properties['workflow_sid']

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._properties['workspace_sid']

    def fetch(self):
        self._context.fetch()

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset):
        self._context.update(
            attributes=attributes,
            assignment_status=assignment_status,
            reason=reason,
            priority=priority,
        )

    def delete(self):
        self._context.delete()

    @property
    def reservations(self):
        return self._context.reservations
