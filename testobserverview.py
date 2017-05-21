from observer import Observer

class TestObserverView(Observer):
    def update(self, *args, **kwargs):
        print("TestObserverForPackets received: {0}\n{1}".format(args, kwargs))