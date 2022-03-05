from ast import pattern
from cgi import print_arguments
from dis import dis
from email.policy import default
from fileinput import filename
from getpass import getpass
from multiprocessing.sharedctypes import Value
import os 
import getpass
import pwd
import stat
from traceback import print_tb
from tracemalloc import stop
import re
from unittest import skip
from isort import file
import platform

from numpy import append

username = os.getlogin()
hostname =  os.popen("hostname").readline()
pwd = os.popen('pwd').readline()


class bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'


def system_info():
    print("System: "+platform.system())
    print("Release"+platform.release())


def user_information(name,host):
    print(f"user name: {name}")
    print(f"hostname: {host}")
    print(f"user info:")
    return os.system(f'id {name}')

def important_files(location,name):

    passwd = "/etc/passwd"
    host = "/etc/hosts"
    shadow = "/etc/shadow"
    bash_history = f"/home/{name}/.bash_history"
    bash_logout = f"/home/{name}/.bash_logout"
    bash_profile = f"/home/{name}/.bash_profile"
    bashrc =  f"/home/{name}/.bashrc"

    list = [passwd,host,shadow,bash_history,bash_logout,bash_profile,bashrc]
    file_name = ["passwd","host","shadow","bash_history","bash_logout","bash_profile","bashrc"]

    try:
        os.system(f"mkdir /home/{name}/linux-information-files")
    except:
        pass

    num = 0
    for u in list:
        try:
            os.system(f"cat {u} >  /home/{name}/linux-information-files/{file_name[num]}.txt ")
            num += 1
        except:
            num += 1
            pass  

    for b in file_name:
        print(bgcolors.OKBLUE+f"file saved: /home/{name}/linux-information-files/{b}.txt "+bgcolors.ENDC)




def sudo_l(name):
    os.system(f"touch /home/{name}/linux-information-files/sudo_l.txt")
    os.system(f"sudo -l > /home/{name}/linux-information-files/sudo_l.txt")
    os.system(f"cat /home/{name}/linux-information-files/sudo_l.txt ")



def file_permission(name):
    # perm_number = os.stat(location)
    # return perm_number.st_mode & stat.S_IRGRP
    # perm_number = os.stat(location)
    # perm = oct(perm_number.st_mode)
    # print(perm)
    # return perm
    passwd = "/etc/passwd"
    host = "/etc/hosts"
    shadow = "/etc/shadow"
    bash_history = f"/home/{name}/.bash_history"
    bash_logout = f"/home/{name}/.bash_logout"
    bash_profile = f"/home/{name}/.bash_profile"
    bashrc =  f"/home/{name}/.bashrc"
    main = "/home/fatkz/Desktop/kod/linux-information/main.py"

    list = [main,passwd,host,shadow,bash_history,bash_logout,bash_profile,bashrc] 
    file_name = ["main","passwd","host","shadow","bash_history","bash_logout","bash_profile","bashrc"]



    for i in list:
        # R_Ok_acces = os.access(f"{i}",os.R_OK)
        perm_file = os.stat(f"{i}")
        # print(oct(f"{perm_file}".st_mode)[-3:]) //error
        mask = oct(os.stat(i).st_mode)[-3:]
        mask_octal = oct(os.stat(i).st_mode)

        picture_perm = stat.filemode(perm_file.st_mode)

        everyone_perm = picture_perm[7:]
        group_perm_x = picture_perm[-6:]
        group_perm = group_perm_x[-3:]
        user_perm = picture_perm[:-6]
        dir_or_file = picture_perm[:-9]

        ## dir or file select if segmant
        if dir_or_file == "-":
            dir_or_file = "file"
        else:
            dir_or_file = "dir"

        
        for a in everyone_perm:
            number = 0
            everyone_tag_write = ""
            everyone_tag_read = ""
            everyone_tag_execute = ""
            while number < len(everyone_perm):
                if everyone_perm[number] == "r":
                    tag_read = "read"
                    number += 1
                elif everyone_perm[number] == "w":
                    tag_write = "write"
                    number += 1
                elif everyone_perm[number] == "x":
                    tag_execute = "execute"
                    number += 1
                elif everyone_perm[number] == "-":
                    number += 1 
                else:
                    stop()

            
            all_everyone_tag_string = everyone_tag_read+"--"+everyone_tag_write+"--"+everyone_tag_execute
            # if len(all_tag_string) < 5:
            #     pattern = r'-'
            #     strings_mod = re.sub(pattern,"",all_tag_string)
            #     print(all_tag_string)
            # print(all_tag_string)

        for c in group_perm:
            number = 0
            group_tag_write = ""
            group_tag_read = ""
            group_tag_execute = ""
            while number < len(group_perm):
                if group_perm[number] == "r":
                    group_tag_read = "read"
                    number += 1
                elif group_perm[number] == "w":
                    group_tag_write = "write"
                    number += 1
                elif group_perm[number] == "x":
                    group_tag_execute = "execute"
                    number += 1
                elif group_perm[number] == "-":
                    number += 1 
                else:
                   stop()

            all_group_tag_string = group_tag_read+"--"+group_tag_write+"--"+group_tag_execute

        for k in user_perm:
            number = 0
            user_tag_write = ""
            user_tag_read = ""
            user_tag_execute = ""
            while number < len(user_perm):
                if user_perm[number] == "r":
                    user_tag_read = "read"
                    number += 1
                elif user_perm[number] == "w":
                    user_tag_write = "write"
                    number += 1
                elif user_perm[number] == "x":
                    user_tag_execute = "execute"
                    number += 1
                elif user_perm[number] == "-":
                    number += 1 
                else:
                   stop()

            all_user_tag_string = user_tag_read+"--"+user_tag_write+"--"+user_tag_execute




        print(bgcolors.RED+f"file: {i}"+f" ({mask})({picture_perm})({dir_or_file}) [everyone:{all_everyone_tag_string}][group:{all_group_tag_string}][user:{all_user_tag_string}]")



def perm_control(file_n):


    list = [] 
    file_name = []

    list.append(file_n)
    file_n = str(file)
    file_name.append(file_n)


    for i in list:
        # R_Ok_acces = os.access(f"{i}",os.R_OK)
        perm_file = os.stat(f"{i}")
        # print(oct(f"{perm_file}".st_mode)[-3:]) //error
        mask = oct(os.stat(i).st_mode)[-3:]
        mask_octal = oct(os.stat(i).st_mode)

        picture_perm = stat.filemode(perm_file.st_mode)

        everyone_perm = picture_perm[7:]
        group_perm_x = picture_perm[-6:]
        group_perm = group_perm_x[-3:]
        user_perm = picture_perm[:-6]
        dir_or_file = picture_perm[:-9]

        ## dir or file select if segmant
        if dir_or_file == "-":
            dir_or_file = "file"
        else:
            dir_or_file = "dir"

        
        for a in everyone_perm:
            number = 0
            everyone_tag_write = ""
            everyone_tag_read = ""
            everyone_tag_execute = ""
            while number < len(everyone_perm):
                if everyone_perm[number] == "r":
                    tag_read = "read"
                    number += 1
                elif everyone_perm[number] == "w":
                    tag_write = "write"
                    number += 1
                elif everyone_perm[number] == "x":
                    tag_execute = "execute"
                    number += 1
                elif everyone_perm[number] == "-":
                    number += 1 
                else:
                    stop()

            
            all_everyone_tag_string = everyone_tag_read+"--"+everyone_tag_write+"--"+everyone_tag_execute
            # if len(all_tag_string) < 5:
            #     pattern = r'-'
            #     strings_mod = re.sub(pattern,"",all_tag_string)
            #     print(all_tag_string)
            # print(all_tag_string)

        for c in group_perm:
            number = 0
            group_tag_write = ""
            group_tag_read = ""
            group_tag_execute = ""
            while number < len(group_perm):
                if group_perm[number] == "r":
                    group_tag_read = "read"
                    number += 1
                elif group_perm[number] == "w":
                    group_tag_write = "write"
                    number += 1
                elif group_perm[number] == "x":
                    group_tag_execute = "execute"
                    number += 1
                elif group_perm[number] == "-":
                    number += 1 
                else:
                   stop()

            all_group_tag_string = group_tag_read+"--"+group_tag_write+"--"+group_tag_execute

        for k in user_perm:
            number = 0
            user_tag_write = ""
            user_tag_read = ""
            user_tag_execute = ""
            while number < len(user_perm):
                if user_perm[number] == "r":
                    user_tag_read = "read"
                    number += 1
                elif user_perm[number] == "w":
                    user_tag_write = "write"
                    number += 1
                elif user_perm[number] == "x":
                    user_tag_execute = "execute"
                    number += 1
                elif user_perm[number] == "-":
                    number += 1 
                else:
                   stop()

            all_user_tag_string = user_tag_read+"--"+user_tag_write+"--"+user_tag_execute




        print(bgcolors.RED+f"file: {i}"+f" ({mask})({picture_perm})({dir_or_file}) [everyone:{all_everyone_tag_string}][group:{all_group_tag_string}][user:{all_user_tag_string}]")


# class find_file():
#     def find_apache_file(username,name):
#         path1 = "/etc/"
#         path2 = "/var/"
#         path3 = "/usr/"
#         list = [path1,path2,path3]
#         for path in list:
#             for root, dirs, files in os.walk(path):
#                 if name in files:
#                     return os.path.join(root, name)


def disk():
    os.system("fdisk -l /dev/null 2>&1")

def open_port(name):
    command_b = "/etc/services"
    print(bgcolors.GREEN+f"[*] {command_b}"+bgcolors.ENDC)

    try:
        command = os.popen(f"cat {command_b}").read()
        command = str(command)
        if command == f"bash: cd: {command_b}: Permission denied":
            perm_control("/etc/services")
        else:
            print(bgcolors.GREEN+f"saved files /home/{name}/linux-information-files/system-service.txt"+bgcolors.ENDC)
            os.system(f" cat {command_b} > /home/{name}/linux-information-files/system-service.txt")
    except:
        skip


def active_port(name):
    comamnd_k = "netstat -tulpn | grep LISTEN"
    comamnd_kk = "netstat -tulpn | grep LISTEN"
    
    # codmant_lbs = os.popen(f"netstat -tulpn | grep LISTEN").read()
    os.system(f" sudo netstat -tulpn | grep LISTEN > /home/{name}/linux-information-files/active-port.txt")
    print(bgcolors.GREEN+f"saved files /home/{name}/linux-information-files/active-port.txt"+bgcolors.ENDC)




# subprocess eklenicek (sonra)
def users_files(name):
    command_files = os.popen(f"cut -d: -f1 /etc/passwd > /home/{name}/linux-information-files/all_users_etc.txt").read()
    list_users_etc = []

    with open(f"/home/{name}/linux-information-files/all_users_etc.txt") as f:
        list_users_etc = [line.rstrip('\n') for line in f]
        os.system(f"mkdir /home/{name}/linux-information-files/users_create_files")

    for i in list_users_etc:
        print(bgcolors.GREEN+"[*]"+f"{i} owner files"+bgcolors.ENDC)
        os.system(f"touch /home/{name}/linux-infsormation-files/users_create_files/{i}.txt ")
        os.system(f" cd / && find . -group {i} -name '*' > /home/{name}/linux-information-files/users_create_files/{i}.txt")
        os.system(f"cat /home/{name}/linux-information-files/users_create_files/{i}.txt")
        print(bgcolors.RED+f"saved files /home/{name}/linux-information-files/users_create_files/{i}.txt"+bgcolors.ENDC)
    print(bgcolors.GREEN+f"All file saved  /home/{name}/linux-information-files/users_create_files/ directory "+bgcolors.ENDC)




    # command_all_system_files = os.system(f"cd / && find . -name '*'  > /home/{name}/linux-information-files/all_files.txt ")
    # print("\r")
    # print(bgcolors.GREEN+f"saved files /home/{name}/linux-information-files/all_files.txt"+bgcolors.ENDC)

    # with open(f"/home/{name}/linux-information-files/all_files.txt") as f:
    #     list_users_file = [line.rstrip('\n') for line in f]
    
    # for i in list_users_file:
    #     os.system(f"ls -la {i}")


    
    

        









    
print(bgcolors.GREEN+"[*] User inFormation: "+bgcolors.ENDC)
print("\r")
user_information(username,hostname)
print("\r")
print(bgcolors.GREEN+"[*] System Info: "+bgcolors.ENDC)
print("\r")
system_info()
print("\r")

print(bgcolors.GREEN+"[/] Important Files: "+bgcolors.ENDC)
print("\r")
important_files(pwd,username)
print("\r")

print(bgcolors.GREEN+"[*] Check ( sudo -l ): "+bgcolors.ENDC)
print("\r")
sudo_l(username)
print("\r")

print(bgcolors.GREEN+"[*] Check (file Permissions): "+bgcolors.ENDC)
print("\r")
file_permission(username)
print("\r")
print(bgcolors.GREEN+"[/] Check (httpd/apache): "+bgcolors.ENDC)
print("\r")
# find_file.find_apache_file("httpd","")
print(bgcolors.GREEN+"[*] Check Disk"+bgcolors.ENDC)
print("\r")
disk()
print("\r")
print(bgcolors.GREEN+"[*] Check system dfult port: "+bgcolors.ENDC)
print("\r")
open_port(username)
print("\r")
print(bgcolors.GREEN+"[*] Check system active port: "+bgcolors.ENDC)
print("\r")
active_port(username)



print(bgcolors.GREEN+"[*] Users Owner files: "+bgcolors.ENDC)
users_files(username)































