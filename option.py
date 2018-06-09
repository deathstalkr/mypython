import time
import os , sys
import webbrowser
import requests
from sel

x='''
Press 1 :  To check current time and date
Press 2 :  To create a  file 
Press 3 :  To create  a directory  
Press 4 :  To logout system
Press 5 :  To  search somehting on google 
Press 6 :  To reboot your OS  
Press  7 :  To  check Internet connectin your PC/LAPPu
Press  8 :  TO LOGIN  whatsupp on browser  ...
press  9  : to  check all connected  IP in your network '''

print(x)
choice =int(input("Enter any number from 1 to 9:"))
if choice ==1:
    print ("Printing current date and time.....")
    print(time.ctime().split()[3])
elif choice==2:
    print("making a file....")
    f = open("xyz.txt", "w+")
    f.close()
elif choice==3:
    path=input('Enter the required path')
    print("Making directory...")
    os.mkdir(path);
elif choice==4:
    os.system("pkill -KILL -u " + os.getlogin())
elif choice==5:
    msg=input('Enter result to search: ')
    print("Searching on google.....")
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg);
elif choice==6:
    print("Rebooting in 20 sec.... please save all the important documents and exit.")
    time.sleep(20);
elif choice==7

else:
    print("Invalid input")