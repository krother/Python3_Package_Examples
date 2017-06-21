
# paramiko

### What it is good for?

Executing commands via SSH.

`paramiko` allows you to execute Unix commands on another machine by logging in via SSH. 
The `fabric` module gives you a comfortable interface built on top of `paramiko`.


### Installed with Python by default

no

### Installed with Anaconda

yes

### Example

List the directory on a remote machine.

    from paramiko import SSHClient
    client = SSHClient()
    client.load_system_host_keys()
    client.connect('ssh.example.com', username="username", password="password")
    stdin, stdout, stderr = client.exec_command('ls -l')

#### WARNING

**Do not hard-code your password inside your Python files. Better read it from a configuration file or environment variable. That way it is less likely that it gets into wrong hands accidentally**

### Where to learn more?

[www.paramiko.org/](http://www.paramiko.org/)
