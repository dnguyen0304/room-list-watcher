# -*- coding: utf-8 -*-

from clare.common import automation


class InitializationFailed(automation.exceptions.AutomationFailed):
    pass


class ExtractFailed(automation.exceptions.AutomationFailed):
    pass
