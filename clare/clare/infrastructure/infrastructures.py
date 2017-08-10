# -*- coding: utf-8 -*-


class RoomListWatcher(object):

    def __init__(self, sender):

        """
        Parameters
        ----------
        sender : typing.Type[clare.common.messaging.producer.senders.Sender]
        """

        self.sender = sender

    def __repr__(self):
        repr_ = '{}(sender={})'
        return repr_.format(self.__class__.__name__, self.sender)


class DownloadBot(object):

    def __init__(self, receiver, deleter):

        """
        Parameters
        ----------
        receiver : typing.Type[clare.common.messaging.consumer.receivers.Buffering]
        deleter : typing.Type[clare.common.messaging.consumer.deleters.Deleter]
        """

        self.receiver = receiver
        self.deleter = deleter

    def __repr__(self):
        repr_ = '{}(receiver={}, deleter={})'
        return repr_.format(self.__class__.__name__,
                            self.receiver,
                            self.deleter)


class Application(object):

    def __init__(self,
                 room_list_watcher_infrastructure,
                 download_bot_infrastructure):

        """
        Parameters
        ----------
        room_list_watcher_infrastructure : clare.infrastructure.infrastructures.RoomListWatcher
        download_bot_infrastructure : clare.infrastructure.infrastructures.DownloadBot
        """

        self.room_list_watcher = room_list_watcher_infrastructure
        self.download_bot = download_bot_infrastructure

    def __repr__(self):
        repr_ = ('{}('
                 'room_list_watcher_infrastructure={}, '
                 'download_bot_infrastructure={})')
        return repr_.format(self.__class__.__name__,
                            self.room_list_watcher,
                            self.download_bot)
