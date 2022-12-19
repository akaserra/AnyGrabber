try:
    import ctypes
    import subprocess, colorama, requests, base64, os, socket
    import sys
    from colorama import Fore, Style
    from pystyle import Center, Colors, Colorate, System, Anime
    import time
except ModuleNotFoundError:
    print("Exception when importing modules")
    print("Installing necessary modules....")
    if os.path.isfile("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip install pystyle")
        os.system("pip install colorama")
        os.system("pip install requests")
    print("Modules installed!")
    time.sleep(1.5)
    os._exit(1

"""
        color
"""
colorama.init()
red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

anydesk_pids = []
anydesk_address = {}
ip_addr = []
old_port = 0
old_ip = ''
banner_loading = """
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░▒▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░▒▓▓▓▓▓▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

"""


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Enjoy")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Enjoy\x07")
    else:
        pass


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    return


def center(var: str, space: int = None):  # From Pycenter
    try:
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2

        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    except OSError:
        print(
            f"{magenta}\nStart the program from a normal terminal.\n{white}If you think it’s a mistake, contact me on discord {lblue}akarta#8573")
        time.sleep(1)
        os._exit(1)


System.Size(60, 30)
Anime.Fade(Center.Center(banner_loading), Colors.red_to_black, Colorate.Vertical, time=2)
subprocess.run('cls || clear', shell=True)

print(center(f"""\r
{Fore.CYAN}(•̪ ●)=︻╦̵̵̿╤─── ⁍ ScreenSharer
            {Fore.LIGHTWHITE_EX}| by akarta#8573 |
    """))
print(lmagenta + "─" * 60)
setTitle("AnyDesk IP Address Resolver • by akarta#8573")

while 1:
    try:
        if str(subprocess.check_output("tasklist")).count('AnyDesk') <= 3:
            pass
        else:
            for line in str(subprocess.check_output("tasklist")).replace('b"', '"').replace('\\r', '').replace('\\n',
                                                                                                               '\n').split(
                '\n'):
                if 'AnyDesk' in line:
                    try:
                        anydesk_pids.append(line.split('.exe')[1].split()[0].replace(' ', ''))

                    except Exception as e:
                        pass
            nstats_output_lines = str(subprocess.check_output('netstat -p TCP -n -a -o')).replace('b"', '"').replace(
                '\\r', '').replace('\\n', '\n').split('\n')
            for pid in anydesk_pids:
                for line in nstats_output_lines:
                    if pid in line and not 'LISTENING' in line:
                        try:
                            parts = line.split()
                            protocol = parts[0]
                            local_addr = parts[1]
                            remote_addr = parts[2].split(':')[0]
                            remote_port = parts[2].split(':')[1]
                            anydesk_address[remote_addr] = int(remote_port)
                        except Exception as e:
                            print(e)
            for ip, port in anydesk_address.items():
                if int(port) > old_port and not '169.254.' in ip:
                    old_port = int(port)
                    old_ip = ip
            remote_ip = old_ip
            remote_port = old_port
            print(f'{lblue} Someone has connected!')


            def ipinfo_command(ip_address):
                """
                Get information about an IP address
                """

                try:
                    socket.inet_pton(socket.AF_INET, ip_address)  # Check the IP address

                    r = requests.get(
                        f'http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,timezone,isp,org,as,asname,reverse,query')
                    r_json = r.json()

                    if r_json['status'] == 'success':
                        continent = r_json['continent']
                        continentCode = r_json['continentCode']
                        country = r_json['country']
                        countryCode = r_json['countryCode']
                        region = r_json['region']
                        regionName = r_json['regionName']
                        city = r_json['city']
                        timezone = r_json['timezone']
                        isp = r_json['isp']
                        org = r_json['org']
                        as_ = r_json['as']
                        asname = r_json['asname']
                        reverse = r_json['reverse']

                        print(f'\n    {magenta}[{lmagenta}I{white}P{magenta}] {white}{remote_ip}')
                        print(
                            f'\n    {magenta}[{lmagenta}Conti{white}nent{magenta}] {white}{continent} ({lmagenta}{continentCode}{white})')
                        print(
                            f'    {magenta}[{lmagenta}Coun{white}try{magenta}] {white}{country} ({lmagenta}{countryCode}{white})')
                        print(
                            f'    {magenta}[{lmagenta}Reg{white}ion{magenta}] {white}{regionName} ({lmagenta}{region}{white})')
                        print(
                            f'    {magenta}[{lmagenta}Ci{white}ty{magenta}] {white}{city} ({lmagenta}{timezone}{white})')
                        print(f'    {magenta}[{lmagenta}IS{white}P{magenta}] {white}{isp} ({lmagenta}{org}{white})')
                        print(
                            f'    {magenta}[{lmagenta}A{white}S{magenta}] {white}{asname} ({lmagenta}{as_}{white})\n')

                        if reverse != '':
                            print(f'    {magenta}[{lmagenta}Reve{white}rse{magenta}] {white}{reverse}\n')

                    else:
                        print(
                            f'\n    {magenta}[{lmagenta}ERR{white}OR{magenta}] {white}The IP address is not valid.')

                except requests.exceptions.ConnectionError:
                    print(f'\n    {magenta}[{lmagenta}ERR{white}OR{magenta}] {white}Could not connect to API.')

                except socket.error:
                    print(f'\n    {magenta}[{lmagenta}ERR{white}OR{magenta}] {white}The IP address is not valid.')


            try:
                ipinfo_command(remote_ip)
            except Exception as e:
                print(f'{lblue}aia. {white + e}')
            print(f'\n\n    {magenta}[{lmagenta}>{magenta}] {lwhite}Closing AnyGrabber... # Created by {lcyan}akarta#8573{reset}')
            input(magenta + 'Press \'enter\' to exit...')
            exit()
    except KeyboardInterrupt:
        print(f'\n\n    {magenta}[{lmagenta}>{magenta}] {lwhite}Closing AnyGrabber... # Created by {lcyan}akarta#8573{reset}')
        exit()

