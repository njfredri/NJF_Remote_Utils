import os
from RemoteUtils import RemoteUtils
print('hello there')

username = input('please input username')
# pwd = input('please enter password') Commented out since not secure. Left here as a reminder not to do so
ssh = input('please input ssh server')

test_dir = os.path.join('/home', username, 'testdir')

RemoteUtils.run_cmd('echo hello', username='njfredri', remote_host='turing.csce.uark.edu', remotedir=test_dir)