# -*- coding: utf-8 -*-

import collections
import datetime
import json
import os
import time

_ENVIRONMENT_VARIABLE_NAME = 'ROOM_LIST_WATCHER_CONFIGURATION_FILE_PATH'


# This implementation closely mirrors the UTC class in pytz and
# subsequently also the one in the Python Standard Library
# documentation.
class UTC(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return datetime.timedelta(0)

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)

    def __str__(self):
        return 'UTC'


class TimeZone(object):

    @classmethod
    def from_name(cls, name):

        """
        Create a tzinfo that corresponds to the specified name.

        Parameters
        ----------
        name : str

        Returns
        -------
        datetime.tzinfo
        """

        return UTC()


class CountdownTimer(object):

    def __init__(self, duration, get_now_in_seconds=None):

        """
        Parameters
        ----------
        duration : float
            The units are in seconds.
        get_now_in_seconds : collections.Callable
            Accepts no arguments and returns a float. Defaults to
            time.time.
        """

        self._duration = duration
        self._get_now_in_seconds = get_now_in_seconds or time.time

        self._start_time = None
        self.is_running = False

    def start(self):
        self._start_time = self._get_now_in_seconds()
        self.is_running = True

    @property
    def has_time_remaining(self):

        """
        Returns
        -------
        bool
            True if there is time remaining.
        """

        now = self._get_now_in_seconds()
        current_duration = now - self._start_time
        has_remaining_time = (self._duration - current_duration) > 0.0
        return has_remaining_time

    def reset(self):
        self._start_time = None
        self.is_running = False

    def __repr__(self):
        repr_ = '{}(duration={}, get_now_in_seconds={})'
        return repr_.format(self.__class__.__name__,
                            self._duration,
                            self._get_now_in_seconds)


def get_configuration():

    """
    Read the application configuration.

    Returns
    -------
    dict
    """

    configuration_file_path = os.environ[_ENVIRONMENT_VARIABLE_NAME]

    with open(configuration_file_path, 'rb') as file:
        parsed_configuration = json.loads(file.read())

    return parsed_configuration


def format_exception(e):

    """
    Parameters
    ----------
    e : exceptions.Exception

    Returns
    -------
    str
    """

    data = collections.OrderedDict()
    data['exception_type'] = type(e).__module__ + '.' + e.__class__.__name__
    data['exception_message'] = e.message

    return json.dumps(data)
