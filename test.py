import os
from RemoteUtils import RemoteUtils
print('hello there')

username = input('please input username: ')
pwd = None #input('please enter password: ') #Commented out since not secure. Left here as a reminder not to do so
ssh = input('please input ssh server: ')

test_dir = os.path.join('/home', username, 'testdir')

RemoteUtils.run_cmd('echo hello', username=username, remote_host=ssh, remotedir=test_dir, remote_password=pwd)

RemoteUtils.run_cmds(['echo hello','echo here', 'echo last'], username=username, remote_host=ssh, remotedir=test_dir, remote_password=pwd)

RemoteUtils.copyFileToServer('./testthing.txt', '/home/njfredri/test', username=username, remote_host=ssh, remote_password=pwd)

RemoteUtils.copyFileFromServer('output.txt', '/home/njfredri/', './output.txt', username=username, remote_host=ssh, remote_password=pwd)