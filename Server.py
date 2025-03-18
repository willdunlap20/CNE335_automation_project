# Will Dunlap
# CNE 335 Winter
# 3/17/2025
# Source code from: ellisju37073 - CNE335_automation_project

import os
import platform

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        system_name = platform.system().lower()

        if system_name == 'windows':
            response = os.system(f"ping -n 4 {self.server_ip}")
        else:
            response = os.system(f"ping -c 4 {self.server_ip}")

        if response == 0:
            return "Server is up!"
        else:
            return "Server is down!"
