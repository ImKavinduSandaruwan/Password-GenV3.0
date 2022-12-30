#Coded by Kavindu Sandaruwan
import random
def option1():
    length = int(input("[*] Enter password legnth you want: "))
    passlist = "ABCDEFGHIJKMNLOPQRSTUVWXYZabcdefghijkmlmnopqrstuvwxyz0123456789!@#$%^&*"
    password = ""
    for i in range(0,length):
        password = random.choice(passlist) + password
    print(password)

choise = 0
def banner():
    print('\033[95m' "██████╗  █████╗  ██████╗ ██████╗ ██╗       ██╗ █████╗ ██████╗ ██████╗        ██████╗ ███████╗███╗  ██╗")
    print('\033[95m' "██╔══██╗██╔══██╗██╔════╝██╔════╝ ██║  ██╗  ██║██╔══██╗██╔══██╗██╔══██╗      ██╔════╝ ██╔════╝████╗ ██║")
    print('\033[95m' "██████╔╝███████║╚█████╗ ╚█████╗  ╚██╗████╗██╔╝██║  ██║██████╔╝██║  ██║█████╗██║  ██╗ █████╗  ██╔██╗██║")
    print('\033[95m' "██╔═══╝ ██╔══██║ ╚═══██╗ ╚═══██╗  ████╔═████║ ██║  ██║██╔══██╗██║  ██║╚════╝██║  ╚██╗██╔══╝  ██║╚████║")
    print('\033[95m' "██║     ██║  ██║██████╔╝██████╔╝  ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║██████╔╝      ╚██████╔╝███████╗██║ ╚███║")
    print('\033[95m' "╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═════╝    ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚═════╝        ╚═════╝ ╚══════╝╚═╝  ╚══╝")
    print('\033[33m'"___________________________________________________________________________ᴄᴏᴅᴇᴅ ʙʏ Kᴀᴠɪɴᴅᴜ Sᴀɴᴅᴀʀᴜᴡᴀɴ"'\033[0m')
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
