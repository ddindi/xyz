import os
import subprocess

def clone(url, name):
    target = os.path.abspath('{}/../data/{}'.format(os.path.dirname(__file__), name))
    
    subprocess.call(['git', 'clone', url, target])
    
    return target
