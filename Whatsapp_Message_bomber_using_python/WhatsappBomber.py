from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time


driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
wait5 = WebDriverWait(driver, 5)
msg = input('Enter the message : ')
count1=int(input('Enter Number of times : '))
target = input('Enter Name of the friend : ')
#targets =['Mona 1','School']
i=0
while(i<count1):
    x_arg = '//span[contains(@title,' +'"' +target + '"' +')]' #.decode('utf-8') 
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()


    message = driver.find_element_by_class_name('_13mgZ')
    message.send_keys(msg)

    sendbutton = driver.find_element_by_class_name('_3M-N-')    
    sendbutton.click()
    i=i+1
driver.close()

