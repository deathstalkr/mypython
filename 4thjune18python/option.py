#!/usr/bin/python2

import  time 
import  webbrowser
import   os
x='''
Press 1 :  To check current time and date
Press 2 :  To create a  file 
Press 3 :  To create  a directory  
Press 4 :  To logout system
Press 5 :  To  search somehting on google 
Press 6 :  To reboot your OS  
Press  7 :  To  check Internet connectin your PC/LAPPu
Press  8 :  TO LOGIN  whatsupp on browser  ...
press  9  : to  check all connected  IP in your network

'''
print  x

choice=raw_input()

if   choice  ==  '1'  :
	print  "showing current time and date ...  ",time.ctime().split()[3]

elif  choice  ==   '5'  :
	print  "searching on Google   ..... "
	msg=raw_input("type to search ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
	
elif  choice ==   '6' :
	print  "close all your apps system is rebootinnnnnnngggggggg ..."
	msg1="acchaa theek hai thoda sa aur time deti huu"
	os.system('echo  '+msg1+'   |   festival  --tts')
	time.sleep(2)
	msg2="are apps band kr na "
	os.system('echo  '+msg2+'   |   festival  --tts')
	time.sleep(3)
	os.system('reboot')
else  :
	print  "wrong option"


