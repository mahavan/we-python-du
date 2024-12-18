"""Develop an app that imitates a server request queue. There should be clients sending requests
to the server, each having its priority. Each new client is queued depending on the priority.
Save the request statistics (user, time) in a separate queue.
Provide statistics output. You can choose the necessary data structures on your own."""
import time
from datetime import datetime

class Server_request_queue:
    def __init__(self):
        self.client = []
        self.log = []

    def queue_push(self, queue, item):
        queue.append(item)
        queue.sort(key=lambda x: (x[0], x[1]))  # sort by priority, then timestamp

    def queue_pop(self, queue):
        if not queue:
            return None
        return queue.pop(0)  # return the first element (highest priority)

    def add_request(self, client_id, priority):
        request_time = time.time()  # Capture the current time
        self.queue_push(self.client, (priority, request_time, client_id))
        print(f"[INFO] Request added: Client={client_id}, Priority={priority}")

    def next_request(self):
        if not self.client:
            print("[INFO] No request.")
            return None

        # pop the request with the highest priority (lowest priority number)
        priority, request_time, client_id = self.queue_pop(self.client)
        readable_time = datetime.fromtimestamp(request_time).strftime('%d-%m-%Y %H:%M:%S')
        log_entry = {
            'client_id': client_id,
            'priority': priority,
            'request_time': readable_time
        }
        self.log.append(log_entry)
        print(f"[INFO] Processed request: {log_entry}")
        return log_entry

    def get_stats(self):
        return self.log

    def display_stats(self):
        if not self.log:
            print("[INFO] No statistics to display.")
            return

        print("[STATISTICS] Processed Requests:")
        for entry in self.log:
            print(
                f"Client: {entry['client_id']}, Priority: {entry['priority']}, Processed Time: {entry['request_time']}")

server = Server_request_queue()

server.add_request("Client1", priority=2)
server.add_request("Client2", priority=1)
server.add_request("Client3", priority=4)
server.add_request("Client4", priority=3)
print()
server.next_request()
server.next_request()
server.next_request()
server.next_request()
print()
server.display_stats()
