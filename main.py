import requests
import time
from termcolor import colored
print(colored('''

██╗      █████╗ ██╗  ██╗ █████╗ ███╗   ██╗ █████╗  ██████╗██╗
██║     ██╔══██╗██║  ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██║
██║     ███████║███████║███████║██╔██╗ ██║███████║██║     ██║
██║     ██╔══██║██╔══██║██╔══██║██║╚██╗██║██╔══██║██║     ██║
███████╗██║  ██║██║  ██║██║  ██║██║ ╚████║██║  ██║╚██████╗██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝
                                                             

                                      > lahanaci webhook spammer

''', 'red'))
print(colored('> LAHANA TOOLS', 'red'))
print()
webhook_url = input("Webhook URL'sini girin: ")
message = input("Spam mesajını girin: ")
delay = float(input("Gecikme süresini girin (saniye olarak): "))
print()

while True:
    response = requests.post(webhook_url, json={"content": message})
    if response.status_code == 204:
        print(colored("Mesaj gönderildi!", 'green'))
    else:
        print("Hata oluştu, mesaj gönderilemedi.")
    time.sleep(delay)
