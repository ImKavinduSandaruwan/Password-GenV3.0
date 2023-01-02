#Coded by Kavindu Sandaruwan
import random
def option1():
    length = int(input("[*] Enter password legnth you want: "))
    passlist = "ABCDEFGHIJKMNLOPQRSTUVWXYZabcdefghijkmlmnopqrstuvwxyz0123456789!@#$%^&*"
    password = ""
    for i in range(0,length):
        password = random.choice(passlist) + password
    print("Your Password is:- ", password)

choise = 0
def banner():
    print('\033[92m' "██████╗  █████╗  ██████╗ ██████╗ ██╗       ██╗ █████╗ ██████╗ ██████╗ '\033[1;33m'       ██████╗ ███████╗███╗  ██╗")
    print('\033[92m' "██╔══██╗██╔══██╗██╔════╝██╔════╝ ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗'\033[1;33m'      ██╔════╝ ██╔════╝████╗ ██║")
    print('\033[92m' "██████╔╝███████║╚█████╗ ╚█████╗  ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║'\033[1;33m'█████╗██║  ██╗ █████╗  ██╔██╗██║")
    print('\033[92m' "██╔═══╝ ██╔══██║ ╚═══██╗ ╚═══██╗  ████╔═████║ ██║  ██║██╔══██╗██║  ██║'\033[1;33m'╚════╝██║  ╚██╗██╔══╝  ██║╚████║")
    print('\033[92m' "██║     ██║  ██║██████╔╝██████╔╝  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝'\033[1;33m'      ╚██████╔╝███████╗██║ ╚███║")
    print('\033[92m' "╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═════╝    ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝ '\033[1;33m'       ╚═════╝ ╚══════╝╚═╝  ╚══╝")
    print('\033[34m'"___________________________________________________________________________ᴄᴏᴅᴇᴅ ʙʏ Kᴀᴠɪɴᴅᴜ Sᴀɴᴅᴀʀᴜᴡᴀɴ"'\033[0m')
    print()
    print()
    print("   [1] Start")
    print("   [2] Update Tool")
    print(" We are recommend to set password length 10 or above to make strong password...")
    print()
    choise = int(input("[*] Enter No:  "))
    print()
    if choise == 1:
        option1()
    else:
        print("You are upto date.....")
banner()
