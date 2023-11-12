import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import hashlib
import webbrowser
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium import webdriver
import requests
import sys
import subprocess
from selenium.webdriver.chrome.options import Options as ChromeOptions
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException




def get_current_script_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))




get = input("get to Web_Siute ------------>")


# نوع الارسال

asd = input(""" 
[1] find_element - Send_Keys
            
[2]  find_element - Click   
            
            
            """)

# نوع العنصر
asd2 = input("""[]----------------->>>>> 
             
             
             
[1] ---->>>>> XPATH

[2] ---->>>>> name  
  
[3] ---->>>>> ID

[4] ---->>>>> By.CLASS_NAME


             """)



# ادخل العنصر


xpath = input("xpath------------>")





options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

options.add_argument('--disable-notifications')

options.add_argument('--ignore-certificate-errors')

options.add_argument('--disable-blink-features=AutomationControlled')

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--auto-open-devtools-for-tabs")
swswewew = 'chromedriver.exe'
file_patswswh = os.path.join(get_current_script_path(), swswewew)  

service = Service(executable_path=file_patswswh)

driver = webdriver.Chrome(service=service, options=options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                            'Chrome/85.0.4183.102 Safari/537.36'})


driver.get(get)

def w():

    driver.implicitly_wait(60)


if "1" in asd:
    

    
    if "1" in asd2:
        w()
        driver.find_element(By.XPATH,xpath).send_keys("By.XPATH")
        w()
        
        
        
    elif "2" in asd2:
        w()
        g =  driver.find_element(By.NAME,xpath)
        g.send_keys("By.NAME")
        w()
    elif "3" in asd2:
        w()
        driver.implicitly_wait(60)
        driver.find_element(By.ID,id).send_keys("By.ID")
        driver.implicitly_wait(60)


    elif "4" in asd2:
        w()
        driver.find_element(By.CLASS_NAME,xpath).send_keys("By.CLASS_NAME")
        driver.implicitly_wait(60)
        w()

else:




    if "1" in asd2:
        w()
        driver.find_element(By.XPATH,xpath).click()
        w()
        
        
        
    elif "2" in asd2:
        w() 
        g =  driver.find_element(By.NAME,xpath)
        g.click()
        w()
    elif "3" in asd2:

        driver.implicitly_wait(60)
        driver.find_element(By.ID,id).click()
        driver.implicitly_wait(60)


    elif "4" in asd2:
        w()
        driver.find_element(By.CLASS_NAME,xpath).click()
        driver.implicitly_wait(60)




time.sleep(9999)





# لا تنسي عايز تسحب كام عنصر عدد العنصر
