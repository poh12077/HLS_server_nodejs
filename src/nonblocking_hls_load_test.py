import requests
import time

res = requests.get("http://192.168.0.124:3000/videos/output.m3u8")
f = open("m3u8.txt", 'w')
f.write(res.text)
f.close()

def parser_m3u8():
	f=open("m3u8.txt",'r')
	while True:
		line = f.readline()
		if not line:break
		elif line[0] != "#":
			line = line[0:-1]
			url = "http://192.168.0.124:3000/videos/" + line
			res = requests.get(url)
			time.sleep(1)
			print( str(res.status_code) + " " + url)
	f.close()

parser_m3u8()
