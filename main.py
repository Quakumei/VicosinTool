from api_client import VkApiClient
import sys
from os import system as sysrun

if __name__ == "__main__" and not('--help' in sys.argv or '-h' in sys.argv):
    if '--token' in sys.argv:
        token = sys.argv[sys.argv.index('--token')+1]
    else:
        token = str(input("Please enter VK token: "))

    print ("Using token --> " + token)
    vkclient = VkApiClient(token)

    # TODO another class for asking for data. 
    # TODO menu (functions and run them)
    # TODO add check for working token (function is ready already)
elif '--help' in sys.argv or '-h' in sys.argv:
    sysrun('cat README.txt | less')
