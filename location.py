import requests
ip=input("enter ip: ")
response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=5df4ea3f9fbc4850b6fbc3fcdb19cf04&ip_adress=",ip)
print("victim",response['ip'])
print("city",response['city'])
