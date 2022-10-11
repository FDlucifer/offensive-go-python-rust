import platform
import getpass
from datetime import datetime

print("computer name: ", platform.node())
print("architecture: ", platform.architecture())
print("running os: ", platform.system())
print("os version: ", platform.release())
print("processor: ", platform.processor())
print("username: ", getpass.getuser())