
# Author : Santosh Kumar
# Github : i-santosh
# Last Update :   21 Aug, 2024
# Tool :   THEN X        
# Description : A simple Python script to install Github hacking tools. It is very easy to use.



import os 
import time

    
def banner():
    print('''

\033[01;31m          ___________________
\033[01;33m————————  ____               \033[01;31m\     
\033[01;33m   | |   |     |\  |   \  /          
\033[01;33m   | |———|——   | \ |    \/          
\033[01;33m   | |   |____ |  \|    /\          
\033[01;31m \___________________  \033[01;33m/  \                                                        
                           

                  \033[01;31mAuthor : SANTOSH KUMAR
                  \033[01;32mGITHUB : i-santosh

''')        
                
banner()


information = [
"Lulz3xploit/LittleBrother","sherlock-project/sherlock","wpscanteam/wpscan","abaykan/trackout","laramies/theHarvester","vanhauser-thc/thc-ipv6","nabla-c0d3/sslyze","moxie0/sslstrip","droe/sslsplit","abbbe/sslcaudit","Cvar1984/sqlscan","s0md3v/sqlmate","sqlmapproject/sqlmap","trustedsec/social-engineer-toolkit","ShawnDEvans/smbmap","lanmaster53/recon-ng","1aN0rmus/TekDefense-Automater","Dionach/CMSmap","Manisso/Crips","shawarkhanethicalhacker/D-TECT","joker25000/Devploit","UndeadSec/EvilURL","FortyNorthSecurity/EyeWitness","T4P4N/IP-FY","zanyarjamal/IP-Locator","Rajkumrdusad/IP-Tracer","maldevel/IPGeoLocation","leapsecurity/InSpy","m4ll0k/Infoga","ciku370/OSIF","behindthefirewalls/Parsero","Tuhinshubhra/RED_HAWK","UltimateHackers/ReconDog","trustedsec/social-engineer-toolkit","aboul3la/Sublist3r","m4ll0k/WAScan","s0md3v/XSStrike","MooseDojo/apt2","royhills/arp-scan","urbanadventurer/bing-ip2hosts","mteg/braa","Zapotek/cdpsnarf","jaygreig86/dmitry","fwaeytens/dnsenum","makefu/dnsmap.","darkoperator/dnsrecon","AeonDave/doork","wireghoul/dotdotpwn","portcullislabs/enum4linux","infobyte/faraday","mschwager/fierce","savio-code/ghost-phisher","golismero/golismero","altjx/ipwn","robertswiecki/intrace","robertdavidgraham/masscan","sullo/nikto","i3visio/osrframework","lanmaster53/recon-ng","6IX7ine/shodanwave","ShawnDEvans/smbmap","trustedsec/social-engineer-toolkit","sqlmapproject/sqlmap","s0md3v/sqlmate","Cvar1984/sqlscan","abbbe/sslcaudit","droe/sslsplit","moxie0/sslstrip","iSECPartners/sslyze","wpscanteam/wpscan"]

vulnerability = [
"zanyarjamal/zambie","shawarkhanethicalhacker/D-TECT","stamparm/DSSS","LOoLzeC/SH33LL","orgcandman/Simple-Fuzzer","s0md3v/Striker","m4ll0k/WAScan","Moham3dRiahi/XAttacker","Manisso/Xshell","Neohapsis/bbqsql","jothatron/blackbox","wireghoul/doona","wireghoul/dotdotpwn","ron190/jsql-injection","CISOfy/lynis","pkg install nmap........","greenbone/openvas","floriankunushevci/rang3r","reverse-shell/routersploit","andyvaikunth/roxysploit","Hadesy2k/sqliv","sqlmapproject/sqlmap","s0md3v/sqlmate","Cvar1984/sqlscan","vanhauser-thc/thc-ipv6","wpscanteam/wpscan","tomac/yersinia"]

exploit = ["rapid7/metasploit-framework","RexTheGod/A-Rat","AlisamTechnology/ATSCAN","Screetsec/Brutal","r00tmars/ExploitOnCLI","Findsploit","r00t-3xp10it/Meterpreter_Paranoid_Mode-SSL","trustedsec/social-engineer-toolkit","a0xnirudh/WebXploiter","Moham3dRiahi/XAttacker","jothatron/blackbox","mikeryan/crackle","ex0dus-0x/dedsploit","nccgroup/demiguise","offensive-security/exploitdb","rand0m1ze/ezsploit","devincrack/MSFinstaller","g0tmi1k/msfpc","reverse-shell/routersploit","andyvaikunth/roxysploit","reyammer/shellnoob","trustedsec/social-engineer-toolkit","sqlmapproject/sqlmap","vanhauser-thc/thc-ipv6","secretsquirrel/the-backdoor-factory","kuburan/txtool","LionSec/xerosploit","thewhiteh4t/flashsploit"]

wireless = ["AresS31/wirespy","JPaulMora/Pyrit","EarToEarOak/RTLSDR-Scanner","P0cL4bs/WiFi-Pumpkin","cinquemb/WifiBruteCrack","nccgroup/Winpayloads","v1s1t0r1sh3r3/airgeddon","joswr1ght/cowpatty","mikeryan/crackle","savio-code/fern-wifi-cracker","FluxionNetwork/fluxion","xtr4nge/giskismet","steve-m/kalibrate-rtl","k4m4/kickthemout","ruped24/killchain","riverloopsec/killerbee","bahaabdelwahed/killshot","zerosum0x0/koadic","sensepost/kwetza","nfc-tools/mfcuk","nfc-tools/mfoc","4ZM/mfterm","EliasOenal/multimon-ng","chrizator/netattack2","chrizator/netattack","wiire-a/pixiewps","esc0rtd3w/wifi-hacker","waseem-sajjad/WifiGod","wifiphisher/wifiphisher","GDSSecurity/wifitap","derv82/wifite2","LionSec/wifresti"]

forensics = ["volatilityfoundation/volatility","keydet89/RegRipper2.8","KeepWannabe/Remot3d","ReFirmLabs/binwalk","simsong/bulk_extractor","aquynh/capstone","cuckoosandbox/cuckoo","gdabah/distorm","6IX7ine/djangohunter"]

webhacking = ["zaproxy/zaproxy","UltimateHackers/Breacher","AonCyberLabs/PadBuster","googleinurl/SCANNER-INURLBR","LOoLzeC/SH33LL","m4ll0k/WAScan","mintobit/WP-plugin-scanner","m4ll0k/WPSeku","OWASP/OWASP-WebScarab","a0xnirudh/WebXploiter","urbanadventurer/WhatWeb","Moham3dRiahi/XAttacker","s0md3v/XSStrike","Manisso/Xshell","bdblackhat/admin-panel-finder","commixproject/commix","SpiderLabs/deblaze","OJ/gobuster","fnord0/hURL","rezasp/joomscan","iniqua/plecost","qunxyz/proxystrike","...","Hadesy2k/sqliv","sqlmapproject/sqlmap","s0md3v/sqlmate","Cvar1984/sqlscan","andresriancho/w3af","hacdias/webdav","zigoo0/webpwn3r","websploit/websploit","xmendez/wfuzz","wpscanteam/wpscan","epsylon/xsser"]

stresstesting = ["Hydra7/Planetwork-DDOS"]

sniffspoof = ["htr-tech/zphisher","4w4k3/KnockMail","lgandx/Responder","trustedsec/social-engineer-toolkit","TunisianEagles/SocialBox","UndeadSec/SocialFish","p4kl0nc4t/Spammer-Grab","Moham3dRiahi/Th3inspector","EgeBalci/The-Eye","Screetsec/TheFatRat","Rajkumrdusad/Tool-X","s0cket7/TorStat","toxic-ig/Trity","4w4k3/Umbrella","Screetsec/Vegile","bettercap/bettercap","Manisso/fsociety","Smaash/fuckshitup","mitmproxy/mitmproxy","r00t-3xp10it/morpheus","Renato-Silva/pyPISHER","EnableSecurity/sipvicious","vecna/sniffjoke","trustedsec/social-engineer-toolkit","evait-security/weeman","epinna/weevely3","mnp/xspy","aydinnyunus/Keylogger","anubhavanonymous/XLR8_BOMBER","Denishnc/b0mb3r","TheSpeedX/TBomb","byt3bl33d3r/MITMf ","DarkSecDevelopers/HiddenEye","avramit/Instahack","Ignitetch/Advphishing","TermuxHackz/anonphisher"]

bruteforce = ["evildevill/instahack","instahackkunal/instahack","KomailKhan/InstaHack","Gameye98/FBBrute","lunnar211/fb-brute","sixtysix-Team/fbbrute","ShuBhamg0sain/Fbbrute","cyb3rt3ch/fb-brute","Oseid/FaceBoom","prahlad01/Fb-Brute","d4az/hack-gmail","adrijano/Gmail-Hack","Ha3MrX/Gemail-Hack","xHak9x/gmailhack","0xfff0800/Brute-force-gmail","Rushi136/gmail-hack","dasithsv/gmail-hack","0xfff0800/Brute-Forc/Twitter","Oseid/TWTBOOM","sadamshr3be/Hack-Twitter","Cyb0r9/Socialbox","Matrix07ksa/Brute_Force"]

password_attack = ["crunchsec/crunch","digininja/CeWL","UltimateHackers/Hash-Buster","magnumripper/JohnTheRipper","trustedsec/social-engineer-toolkit","danielmiessler/SecLists","UndeadSec/SocialFish","moyix/creddump","lightos/credmap","galkan/crowbar","Mebus/cupp","CiKu370/hash-generator","hashcat/hashcat","galauerscrew/hasherdotid","CiKu370/hasher","pkg install hydra.....","shinnok/johnny","inquisb/keimpx","hashcat/maskprocessor","trustedsec/social-engineer-toolkit"]

maintaining = ["trustedsec/ridenum","deadbits/Intersect-2.5","PowerShellMafia/PowerSploit","durandal/dbd","larsbrinkhoff/httptunnel","samratashok/nishang","samyk/pwnat"]

iptracking = ["abaykan/trackout","T4P4N/IP-FY","zanyarjamal/IP-Locator","Rajkumrdusad/IP-Tracer","maldevel/IPGeoLocation","leapsecurity/InSpy","m4ll0/Infoga","boxug/trape"]

programming = ["c++","clang","c","golang","nodejs","perl","php","python","ruby","lua","nasm"]

ddos = ["darkwarrior3/hulk","D35m0nd142/LFISuite","BaSai-Ddos/LITEDDOS","bangnaga1/Litespam","Gameye98/Lazymux","cyweb/hammer"]

termux_desktop = ["adi1090x/termux-desktop"]

linux_os = ["pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpinexfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh | bash","pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh | bash"]

extra = ["thewhiteh4t/killcast","Hackplayers/4nonimizer ","ASHWIN990/ADB-Toolkit","AndroBugs/AndroBugs_Framework","TunisianEagles/Androspy","nxxxu/AutoPixieWps","Gameye98/Auxscan","engMaher/BAF","MrSqar-Ye/BadMod","4w4k3/BeeLogger","Gameye98/Black-Hydra","UltimateHackers/Blazy","tiagorlampert/CHAOS","Tuhinshubhra/CMSeeK","D4Vinci/Clickjacking-Tester","Xyl2k/Cookie-stealer","abaykan/CrawlBox","ustayready/CredSniper","medbenali/CyberScan","Mr-Un1k0d3r/DKMC","stamparm/DSVW","stamparm/DSXS","D4Vinci/Dr0p1t-Framework","Screetsec/Dracnmap","ThoughtfulDev/EagleEye","sabri-zaki/EasY_HaCk","neoneggplant/EggShell","Juniorn1003/Email-Spammer","EmpireProject/Empire","mrSilent0598/FBUPv2.0","Ha3MrX/Gemail-Hack","StreetSec/Gloom-Framework","UndeadSec/GoblinWordGenerator","SilentGhostX/HT-WPS-Breaker","mehedishakeel/HTools","MetaChar/Hatch","b3-v3r/Hunner","PowerScript/KatanaFramework","Screetsec/LALIN","MetaChar/Mercury","micle-fm/Parat","WiPi-Hunter/PiDense","SilverFoxx/PwnSTAR","ikkebr/PyBozoCrack","Ekultek/Pybelt","OWASP/QRLJacking","1N3/ReverseAPK","m4ll0k/SMBrute","1N3/Sn1per","nathanlopez/Stitch","Souhardya/Zerodoor","Wh1t3Rh1n0/air-hammer","ihebski/angryFuzzer","govolution/avet","bleachbit/bleachbit","x90skysn3k/brutespray","ring0lab/catphish","susmithHCK/cpscan","s0lst1c3/eaphammer","D4Vinci/elpscrk","peterpt/eternal_scanner","kgretzky/evilginx","chinoogawa/fbht","Tuhinshubhra/fbvid","almandin/fuxploider","twelvesec/gasmask","byt3bl33d3r/gcat","peterpt/get","thehackingsage/hacktronian","4shadoww/hakkuframework","SpiderLabs/jboss-autopwn","tearsecurity/leviathan","arismelachroinos/lscript","robertdavidgraham/masscan","s0cket7/nWatch","alexxy/netdiscover","esmog/nodexp","1tayH/noisy","k4m4/onioff","jesparza/peepdf","n1nj4sec/pupy","karulis/pybluez","LandGrey/pydictor","linkedin/qark","citronneur/rdpy","tiagorlampert/sAINT","cys3c/secHub","Tuhinshubhra/shellstack","cyberark/shimit","s0cket7/smap","m8r0wn/subscraper","susmithHCK/torghost","r00t-3xp10it/trojanizer","siruidops/uidsploit","EnableSecurity/wafw00f","bytezcrew/wfdroid-termux","JamesJGoodwin/wreckuests","hatRiot/zarp","pasahitz/zirikatu","ZechBron/zVirus-Gen"]

#def git_url(url):
#    return os.system(f'git clone https://github.com/{links[sel]}.git')


def complete():
    print("******Tool Successfully Installed!******\n")
    return time.sleep(2)
    
    
def clear():
    os.system("clear") 
    

def invalid():
    print("____Invalid Choice!____\n")
    time.sleep(2)

# Main Functions Starts here
             
    
sel_catg = True
while (sel_catg!=0):
    clear()
    banner()
    print('''______________________________
                             |''')
                             
                             
    with open("category.txt") as f:
        category = f.read()
        print(category)
        sel_catg = int(input("\nSelect Tool category: "))
        if (sel_catg==0):  # select 0 
            exit()
        elif (sel_catg==1): # select 1
            with open("information.txt") as f:
                info = f.read()
                choice1 = True
                while (choice1!=70):
                    print("---------------------------------------")
                    print(info)
                    choice1 = int(input("Entre tool: "))
                    if choice1>=71:
                        invalid()
                    for a in range(70):
                        if choice1 == a:
                            os.system(f'git clone https://github.com/{information[choice1]}.git')
                            complete()
        elif (sel_catg==2): # select 2
            with open("vulnerability.txt") as f:
                vulner = f.read()
                choice2 = True
                while (choice2!=27):
                    print("---------------------------------------")
                    print(vulner)
                    choice2 = int(input("Entre tool: "))
                    if choice2>=28:
                        invalid()
                    for a in range(27):
                        if choice2 == a:
                            os.system(f'git clone https://github.com/{vulnerability[choice2]}.git')
                            complete()
        elif (sel_catg==3): # select 3
            with open("exploitations.txt") as f:
                exploit = f.read()
                choice3 = True
                while (choice3!=30):
                    print("---------------------------------------")
                    print(exploit)
                    choice3 = int(input("Entre tool: "))
                    if choice3>=31:
                        invalid()
                    for a in range(30):
                        if choice3 == a:
                            os.system(f'git clone https://github.com/{exploit[choice3]}.git')
                            complete()
        elif (sel_catg==4): # select 4
            with open("wireless.txt") as f:
                wireless = f.read()
                choice4 = True
                while (choice4!=32):
                    print("---------------------------------------")
                    print(wireless)
                    choice4 = int(input("Entre tool: "))
                    if choice4>=33:
                        invalid()
                    for a in range(32):
                        if choice4 == a:
                            os.system(f'git clone https://github.com/{wireless[choice4]}.git')
                            complete()
        elif (sel_catg==5): # select 5
            with open("forensics.txt") as f:
                forensics = f.read()
                choice5 = True
                while (choice5!=9):
                    print("---------------------------------------")
                    print(forensics)
                    choice5 = int(input("Entre tool: "))
                    if choice5>=10:
                        invalid()
                    for a in range(9):
                        if choice5 == a:
                            os.system(f'git clone https://github.com/{forensics[choice5]}.git')
                            complete()
        elif (sel_catg==6): # select 6
            with open("webhacking.txt") as f:
                web = f.read()
                choice6 = True
                while (choice6!=34):
                    print("---------------------------------------")
                    print(web)
                    choice6 = int(input("Entre tool: "))
                    if choice6>=35:
                        invalid()
                    for a in range(34):
                        if choice6 == a:
                            os.system(f'git clone https://github.com/{webhacking[choice6]}.git')
                            complete()
        elif (sel_catg==7): # select 7
            with open("stresstesting.txt") as f:
                stress = f.read()
                choice7 = True
                while (choice7!=1):
                    print("---------------------------------------")
                    print(stress)
                    choice7 = int(input("Entre tool: "))
                    if choice7>=2:
                        invalid()
                    for a in range(1):
                        if choice7 == a:
                            os.system(f'git clone https://github.com/{stresstesting[choice7]}.git')
                            complete()
        elif (sel_catg==8): # select 8
            with open("sniffspoof.txt") as f:
                sniff = f.read()
                choice8 = True
                while (choice8!=36):
                    print("---------------------------------------")
                    print(sniff)
                    choice8 = int(input("Entre tool: "))
                    if choice8>=37:
                        invalid()
                    for a in range(36):
                        if choice8 == a:
                            os.system(f'git clone https://github.com/{sniffspoof[choice8]}.git')
                            complete()
        elif (sel_catg==9): # select 9
            with open("passwordattack.txt") as f:
                passwd = f.read()
                choice9 = True
                while (choice9!=20):
                    print("---------------------------------------")
                    print(passwd)
                    choice9 = int(input("Entre tool: "))
                    if choice9>=21:
                        invalid()
                    for a in range(20):
                        if choice9 == a:
                            os.system(f'git clone https://github.com/{password_attack[choice9]}.git')
                            complete()
        elif (sel_catg==10): # select 10
            with open("maintaining.txt") as f:
                maintain = f.read()
                choice10 = True
                while (choice10!=7):
                    print("---------------------------------------")
                    print(maintain)
                    choice10 = int(input("Entre tool: "))
                    if choice10>=8:
                        invalid()
                    for a in range(7):
                        if choice10 == a:
                            os.system(f'git clone https://github.com/{maintaining[choice10]}.git')
                            complete()
        elif (sel_catg==11): # select 11
            with open("iptracking.txt") as f:
                iptrack = f.read()
                choice11 = True
                while (choice11!=8):
                    print("---------------------------------------")
                    print(iptrack)
                    choice11 = int(input("Entre tool: "))
                    if choice11>=9:
                        invalid()
                    for a in range(8):
                        if choice11 == a:
                            os.system(f'git clone https://github.com/{iptracking[choice11]}.git')
                            complete()
        elif (sel_catg==12):# select 12
            with open("programming.txt") as f:
                program = f.read()
                choice12 = True
                while (choice12!=11):
                    print("---------------------------------------")
                    print(program)
                    choice12 = int(input("Entre tool: "))
                    if choice12>=12:
                        invalid()
                    for a in range(11):
                        if choice12 == a:
                            os.system(f'pkg install {programming[choice12]}')
                            complete()
        elif (sel_catg==13):# select 13
            with open("ddos.txt") as f:
                ddos = f.read()
                choice13 = True
                while (choice13!=6):
                    print("---------------------------------------")
                    print(ddos)
                    choice13 = int(input("Entre tool: "))
                    if choice13>=7:
                        invalid()
                    for a in range(6):
                        if choice13 == a:
                            os.system(f'git clone https://github.com/{ddos[choice13]}.git')
                            complete()
        elif (sel_catg==14):# select 14
            with open("termuxos.txt") as f:
                termuxos = f.read()
                choice14 = True
                while (choice14!=1):
                    print("---------------------------------------")
                    print(termuxos)
                    choice14 = int(input("Entre tool: "))
                    if choice14>=2:
                        invalid()
                    for a in range(1):
                        if choice14 == a:
                            os.system(f'git clone https://github.com/{termux_desktop[choice14]}.git')
                            complete()
        elif (sel_catg==15):# select 15
            with open("linuxos.txt") as f:
                linux = f.read()
                choice15 = True
                while (choice15!=8):
                    print("---------------------------------------")
                    print(linux)
                    choice15 = int(input("Entre tool: "))
                    if choice15>=9:
                        invalid()
                    elif choice15 == 0:
                            os.system(f"git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
                    for a in range(1,8):  
                        if choice15 == a:
                            os.system(linux_os[choice15])
                            complete()
        elif (sel_catg==16):# select 16
            with open("extra.txt") as f:
                extra = f.read()
                choice16 = True
                while (choice16!=100):
                    print("---------------------------------------")
                    print(extra)
                    choice16 = int(input("Entre tool: "))
                    if choice16>=101:
                        invalid()
                    for a in range(100):
                        if choice16 == a:
                            os.system(f'git clone https://github.com/{extra[choice16]}.git')
                            complete()
        elif (sel_catg==17):
            with open("Bruteforce.txt") as f:
                brute = f.read()
                choice17 = True
                while (choice17!=22):
                    print("---------------------------------------")
                    print(brute)
                    choice17 = int(input("Entre tool: "))
                    if choice17>=23:
                        invalid()
                    for a in range(22):
                        if choice17 == a:
                            os.system(f'git clone https://github.com/{bruteforce[choice17]}.git')
                            complete()              
                            
        elif (sel_catg>=18):
            invalid()
