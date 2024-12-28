import subprocess


class RemoteUtils:
    def run_cmd(cmd_str, username, remote_host, remote_password:str = None, remotedir:str = None):
        """
        runs command string in a remote bash shell
        """
        print("Command: %s" %(cmd_str))
        
        ssh_call = 'ssh ' + username + '@' + remote_host
        if remote_password != None:
            sshpass = 'sshpass -p' + "'" + remote_password + "'"
            ssh_call = sshpass + ' ' + ssh_call
        
        print(ssh_call)
        # subprocess.call(cmd_str,shell=True,executable="/bin/bash")

    def copyFileToServer(file, remotedir, username, remote_host, remote_password:str = None):
        command = 'scp ' + file + ' ' + username + '@' + remote_host + ':' + remotedir
        if remote_password != None:
            command = 'sshpass -p ' + remote_host + ' ' + command
        RemoteUtils.run_cmd(command)


        