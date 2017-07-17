import requests
conn = requests.Session();
m="FC:FB:FB:01:FA:21"
def mac_decode(mac):
	str="https://api.macvendors.com/"+mac
	c = conn.get(str)
	return c.content
try:
  print  mac_decode(m)
except:
	print "error"
