import os, sys
import time
import webbrowser
import socket
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

x='''
Press 1 :  To check current time and date
Press 2 :  To create a  file 
Press 3 :  To create  a directory  
Press 4 :  To logout systemps | ctrlc
Press 5 :  To search somehting on google 
Press 6 :  To reboot your OS  
Press 7 :  To check Internet connectiON your PC/LAPTOP
press 8 :  To check all connected  IP in your network
Press 9 :  TO LOGIN  whatsApp on browser  ...'''

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
elif choice==7:
    print('Have patience..we are checking your internet connection...')
    hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)

    #check the response...
    if response == 0:
        print('Congrats!! Your have active internet connection...')
    else:
        print('Sorry!! Please check your internet connection and try again....')

elif choice==8:
    print("Getting list of all the connected IP's....please wait...")
    print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

elif choice==9:
    def message(Rejoice,message='hi its me'):
     """this a simple function to send a whatsapp message to your friends
    and group using python and selenium an automated tool to parse the HTML
    content and to change the properties.
    paramters:
    to - enter a name from your contacts it can be friend's name or a group's title
    message - message to be deliever"""
    d = webdriver.Chrome(r'/usr/bin/chromedriver')		# directory to chromedriver
    d.get('https://web.whatsapp.com/')					# URL to open whatsapp web
    wait = WebDriverWait(driver = d, timeout = 900)			# inscrease or decrease the timeout according to your net connection
                                                                # additional text to with your message to identify that it is send via software

    name_argument = f'//span[contains(@title,\'{Rejoice}\')]'		# HTML parse code to identify your reciever
    title = wait.until(EC.presence_of_element_located((By.XPATH,name_argument)))
    title.click()							# to open the receiver messages page in the browser

    # many a times class name or other HTML properties changes so keep a track of current class name for input box by using inspect elements
    input_path = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
    box = wait.until(EC.presence_of_element_located((By.XPATH,input_path)))

    box.send_keys(message + Keys.ENTER)					# send your message followed by an Enter


else:
    print("Invalid input")
