import asyncio

from singleton.singleton import ThreadSafeSingleton


@ThreadSafeSingleton
class EventBus:
    listeners = {}

    def add_listener(self, event_name, listener):
        if not self.listeners.get(event_name, None):
            self.listeners[event_name] = {listener}
        else:
            self.listeners[event_name].add(listener)

    def remove_listener(self, event_name, listener):
        self.listeners[event_name].remove(listener)
        if len(self.listeners[event_name] == 0):
            del self.listeners[event_name]

    def emit(self, event_name, event):
        lsnrs = self.listeners.get(event_name, [])
        for lnsr in lsnrs:
            asyncio.run(lnsr(event))

