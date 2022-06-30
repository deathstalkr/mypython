from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
driver = webdriver.Chrome(r'/usr/bin/chromedriver')
driver.get('https://chart-builder.data.world/?agentid=cancerdatahp&datasetid=lung-cancer-data&query=SELECT%20%2A%0AFROM%20cancer_patient_data_sets&query_type=SQL')

x=input("Enter the X-coordinate element:")
y=input("Enter the Y-coordinate element:")
wait = WebDriverWait(driver = driver, timeout = 900)

x_box=driver.find_element_by_class_name("css-1492t68")
x_box.send_keys(x)
pyautogui.press("Enter")

y_box=driver.find_element_by_class_name("css-1492t68")
y_box.send_keys(y)
pyautogui.press("Enter")


