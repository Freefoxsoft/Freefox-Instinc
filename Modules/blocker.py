import platform

def blocker():
    if platform.system() == "Windows":
        pathToHosts = r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == "Linux":
        pathToHosts = r"/etc/hosts"

    redirect = "127.0.0.1"
    websites = ["www.adfpoint.com","www.passeura.com","www.dirtyleague.com","www.ultimateaderaser.com","www.d1gpk60s9m56kt.cloudfront.net","www.youporn.com","www.iyfbodn.com","www.notfcompreviews.com","ultimateaderaser.com","www.bongacams.com","fr.bongacams.com","bongacams.com","www.wyylde.com","wyylde.com","mommygravelyslime.com","www.mommygravelyslime.com",
                "www.compare24.net","compare24.net"
    ]
    with open(pathToHosts, 'r+') as file:
        content = file.read()
        for site in websites:
            if site in content:
                pass
            else:
                file.write(redirect + " " + site + "\n")