# Will Dunlap
# CNE 335 Winter
from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Will Dunlap")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("52.38.252.235")
    response = server.ping()
    print("Ping response:", response)
