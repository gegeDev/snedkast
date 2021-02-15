import os
import subprocess
def mkdir(name):
    try: os.mkdir(name)
    except FileExistsError: pass
