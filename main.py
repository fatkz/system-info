from ast import pattern
from email.policy import default
from fileinput import filename
from getpass import getpass
from multiprocessing.sharedctypes import Value
import os 
import getpass
import pwd
import stat
from tracemalloc import stop
import re
from isort import file
import platform

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



class find_file():
    def find_apache_file(username,name):
        path1 = "/etc/"
        path2 = "/var/"
        path3 = "/usr/"
        list = [path1,path2,path3]
        for path in list:
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)





    
print(bgcolors.GREEN+"-----------------------User inFormation----------------------------------------"+bgcolors.ENDC)
user_information(username,hostname)

print(bgcolors.GREEN+"-----------------------System Info----------------------------------------"+bgcolors.ENDC)
system_info()

print(bgcolors.GREEN+"-----------------------------Important Files----------------------------------"+bgcolors.ENDC)
important_files(pwd,username)

print(bgcolors.GREEN+"-----------------------------Check ( sudo -l )----------------------------------"+bgcolors.ENDC)
sudo_l(username)

print(bgcolors.GREEN+"-----------------------------Check (file Permissions)----------------------------------"+bgcolors.ENDC)
file_permission(username)

print(bgcolors.GREEN+"-----------------------------Check (httpd/apache)----------------------------------"+bgcolors.ENDC)
find_file.find_apache_file("httpd","")



# print(bgcolors.WARNING+"test"+bgcolors.ENDC)































































