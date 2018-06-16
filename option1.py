import os, sys
import time
import webbrowser
import socket
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
x='''
Press 1 :  To check current time and date
Press 2 :  To create a  file 
Press 3 :  To create  a directory  
Press 4 :  To logout of system 
Press 5 :  To search somehting on google 
Press 6 :  To reboot your OS  
Press 7 :  To check Internet connection of your PC/LAPTOP
press 8 :  To check all connected  IP in your network 
Press 9 :  TO LOGIN into whatsapp on browser  ...'''

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
    print('Sit back..loging out!!')
    os.system("pkill -KILL -u " + os.getlogin())
elif choice==5:
    msg=input('Enter result to search: ')
    print("Searching on google.....")
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg);
elif choice==6:
    print("Rebooting in 20 sec.... please save all the important documents and exit.")
    time.sleep(20);
    os.system('reboot')
elif choice==7:
    print('Have patience..we are checking your internet connection...')
    hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)

    #check the response...
    if response == 0:
        print('\n\nCongrats!! Your have active internet connection...')
    else:
        print('\n\nSorry!! Please check your internet connection and try again....')

elif choice==8:
    print("Getting list of all the connected IP's....please wait...")
    print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

elif choice==9:
    driver = webdriver.Chrome(r'/usr/bin/chromedriver')
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))
    wait = WebDriverWait(driver = driver, timeout = 900)
    #input('Click anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
       msg_box.send_keys(msg)
       button = driver.find_element_by_class_name('_2lkdt')
       button.click()


else:
    print("Invalid input")
