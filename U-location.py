import requests, json
import os
import sys
#Colours that i will use
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
os.system("clear")
os.system("figlet U-danbaiwa")
print(cy+"\t\t\tv 1.0.0")
print("")
print("1:- IP INFORMATION")
print("")
print("2:- UPDATE TOOL")
print("")
for i in range(90):
	com=input("Enter Choice: ")
	if com=="1":
		os.system("clear")
		os.system("figlet IP-INFO...")
		print(green+"\t\t\tv 1.0.0")
		print(cya+"\t\t   coded By U-danbaiwa")
		print("")
		print("")
		ip=input(green+bold+"[*] Enter Victim Ip:  ")
		response ="http://ip-api.com/json/"
		re=requests.get(response+ip).json()
		print("")
		print("")
		print(yellow+bold+"**********************VICTIM INFORMATION********************")
		print(red+"[ * ] Victim ip:<=====>",re["query"])
		print("")
		print(cyan+"[ * ] Status Code:<=====>",re["status"])
		print("")
		print(cy+"[ * ] Victim Country:<=====>",re["country"])
		print("")
		print(cya+"[ * ] Victim Country_Code:<=====>",re['countryCode'])
		print("")
		print(cyan+"[ * ] Victim Region:<=====>",re["region"])
		print("")
		print(green+"[ * ] Victim RegionName:<=====>",re["regionName"])
		print("")
		print(cy+"[ * ] Victim City:<=====>",re["city"])
		print("")
		print(green+"[ * ] Latitude:<=====>"+re["Lat"])
		print("")
		print(cy+"[ * ] Longitude:<=====>",re["lon"])
		print("")
		print(red+"[ * ] Victim TimeZone:<=====>",re["timezone"])
		print("")
		#print(green+"[ * ] Victim Currency:<=====>",re["currency"])
		print("")
		print(cyan+"[ * ] Victim Isp:<=====>",re["isp"])
		print("")
		print(cy+"[ * ] Victim Org:<=====>",re["org"])
		print("")
		print(cya+"[ * ] Victim As:<=====",re["as"])
		print("")
		print(green+"[ * ] Victim Zip Code:<=====>",re["zip"])
		print("")
		print(red+"[ * ] Victim Messega<=====>",["message"])
		print("")
		print(red+"\n\n\t\t\tSHARE AND FOLLOW US FOR MORE TOOLS")
	elif com=="2":
	       os.system("clear")
	       os.system("figlet U-danbaiwa")
	       print("please wait...")
	       os.system("cd /data/data/com.termux/files/home")
	       os.system("pkg update -y")
	       os.system("pkg install -y git")
	       os.system("pkg install python2")
	       os.system("cd /data/data/com.termux/files/home && git clone https://github.com/U-danbaiwa/location.git")
	       os.system("cd /data/data/com.termux/files/home")
	       print(cya+"\t=====COMPLETE INSTALL THANK YOU=====")
	else:
		print("invalid command!")
