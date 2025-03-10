import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        response = os.system(f"sudo ping -c 4 {self.server_ip}")
        if response == 0:
            return "Server is up!"
        else:
            return "Server is down!"
