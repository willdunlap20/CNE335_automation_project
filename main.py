# Will Dunlap
# CNE 335 Winter
# 3/17/2025
# Source code from: ellisju37073 - CNE335_automation_project 'https://github.com/ellisju37073/CNE335_automation_project'

from Server import Server

def print_program_info():
    print("Server Automator by Will Dunlap")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("52.38.252.235")
    response = server.ping()
    print("Ping response:", response)
