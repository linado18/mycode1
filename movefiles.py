#!/use/bin/env python3

##Moving files with sftp

##import paramiko so we can talk ssh
import paramiko
import os

##where to connect to
t = paramiko.Transport("10.10.2.3", 22)

##how to connect
t.connect(username="bender", password="alta3"

#instatiate sftp
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/file04.log', '/home/student/file04copied.py'

##iterate across files in a directory
for x in os.listdir("/home/student/filescopy/"): #iterate on directory contents
    if not os.path.isdir("/home/student/filecopy/"+x): #filter out anything that is NOT a dir
        sftp.put("/home/student/filescopy/"+x, "/tmp/"+x #move files from student to target
sftp.close()
