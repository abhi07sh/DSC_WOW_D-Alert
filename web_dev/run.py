import socket
REMOTE_SERVER = "one.one.one.one"

def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False
if not is_connected(REMOTE_SERVER):
	print("No Internet Connection")
	# exit()

from flaskblog import app


if __name__ == '__main__':
    app.run(debug=True)
