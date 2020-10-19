class Event:
    def __init__(self,event_id,name):
        self.event_id = event_id
        self.name = name

    def execute(self):
        raise NotImplementedError()

class ManualStartEvent(Event):
    def __init__(self,bgp,address,asn,port=179):
        super().__init__(1,"Manual Start")
        self.bgp = bgp
        self.address = address
        self.asn = asn
        self.port = port

    def execute(self):
        peer = self.bgp.add_peer(self.address,self.asn,self.port)
        peer.init_client_connection()
        peer.send_open_message()
        peer.get_messages()
        


class ManualStopEvent(Event):
    def __init__(self, bgp, peer):
        super().__init__(2,"Manual Stop")
        self.bgp = bgp
        self.peer = peer

    def execute(self, peer):
        peer = self.bgp.remove_peer(self.peer)
        peer.disconnect()
