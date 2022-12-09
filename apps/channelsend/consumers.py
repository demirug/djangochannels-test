from channels.consumer import SyncConsumer


class ChannelTest(SyncConsumer):
    def log_msg(self, e):
        print(f"Incoming data: {e['message']}")