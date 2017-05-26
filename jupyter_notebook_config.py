c=get_config()
c.NotebookApp.password=u'sha1:c272b2500f51:8d9154e2f3a20b15386f2073991d9c7a4d0aa86e'
c.NotebookApp.certfile = u'/home/ec2-user/.jupyter/mycert.pem'
# The full path to a private key file for usage with SSL/TLS.
c.NotebookApp.keyfile = u'/home/ec2-user/.jupyter/mycert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False