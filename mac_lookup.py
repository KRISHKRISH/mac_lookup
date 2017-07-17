import requests
conn = requests.Session();
m="FC:FB:FB:01:FA:21"
headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language" : "en-US,en;q=0.5","Accept-Encoding" : "gzip, deflate","Connection": "keep-alive","Upgrade-Insecure-Requests": "1","Cache-Control": "max-age=0"}
def mac_decode(mac):
	str="https://api.macvendors.com/"+mac
	c = conn.get(str,headers=headers)
	return c.content
try:
  print  mac_decode(m)
except:
	print "error"