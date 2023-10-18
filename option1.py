import os
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
    print(time.ctime().split()[3])      #prints only the time by emove al others
elif choice==2:
    print("making a file....")
    f = open("xyz.txt", "w+")   #makes the file
    f.close()                     #and saves then exits
elif choice==3:
    path=input('Enter the required path')
    print("Making directory...")
    os.mkdir(path);          #makes tke directory in the required path
elif choice==4:
    print('Sit back..loging out!!')
    os.system("pkill -KILL -u " + os.getlogin())   #logging out of the system by killing all the opened application
elif choice==5:
    msg=input('Enter result to search: ')
    print("Searching on google.....")
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg);   #searches the google using web crawler 'q'
elif choice==6:
    print("Rebooting in 20 sec.... please save all the important documents and exit.")
    time.sleep(20);          #delays boot-time
    os.system('reboot')     #reboots system
elif choice==7:
    print('Have patience..we are checking your internet connection...')
    hostname = "www.google.com"
    response = os.system("ping -c 5 " + hostname)     #sends 5 packets to the google ......

    #check the response...
    if response == 0:
        print('\n\nCongrats!! Your have active internet connection...')
    else:
        print('\n\nSorry!! Please check your internet connection and try again....')

elif choice==8:
    print("Getting list of all the connected IP's....please wait...")
    print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

elif choice==9:
    driver = webdriver.Chrome(r'/usr/bin/chromedriver')    #enter the location of the chromedriver
    driver.get('https://web.whatsapp.com/')                #opens the website

    name = input('Enter the name of user or group : ')      #input recipient name
    msg = input('Enter your message : ')                    #input message
    count = int(input('Enter the count : '))                 #input numbet of times the message is to be sent
    wait = WebDriverWait(driver = driver, timeout = 900)      #wait till the QR code is scanned and the chat page is opened ...time keeps on increasing according to the connection
    #input('Click anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))     #searches for the reciver and enters into the chatpage
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')                  #enters message into the chat box

    for i in range(count):                                  #loop to send the message count times
       msg_box.send_keys(msg)
       button = driver.find_element_by_class_name('_2lkdt')         #click on send button
       button.click()


else:
    print("Invalid input. Please try again..")                                   #returns  if invalid input is detected

