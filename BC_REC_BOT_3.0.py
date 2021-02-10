#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import getpass
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from os import environ


# In[18]:


USERNAME_KEY = environ ['USERNAME_KEY']
PASS_KEY = environ ['PASS_KEY']


# In[19]:


def book ():
     #Open login dialog 
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    gDriver = webdriver.Chrome(
        chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
    gDriver.get("https://recconnect.bc.edu")
    time.sleep(1)
    gDriver.execute_script('document.querySelector("#loginLink-mobile").click()')
    time.sleep(1)
    
    #Login to reconnect.bc.edu
    username_box = gDriver.find_element_by_css_selector ('#txtUsername')
    username_box.send_keys(USERNAME_KEY)
    password_box = gDriver.find_element_by_css_selector ('#txtPassword')
    password_box.send_keys(PASS_KEY)
    gDriver.find_element_by_css_selector ('#btnLogin').click()
    

    gDriver.execute_script("window.open('');")
    gDriver.switch_to.window(gDriver.window_handles[1])
    gDriver.get('https://recconnect.bc.edu/booking/93a7d382-156f-472c-bf90-006fb897d1c4')
    element = gDriver.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
    actions = ActionChains(gDriver)
    actions.move_to_element(element).perform()
    element.click()
    day = gDriver.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]').get_attribute("data-day")
    initial_day = int(day)
    gDriver.close()
    gDriver.switch_to.window(gDriver.window_handles[0])
    
    def check_date ():
        gDriver.execute_script("window.open('');")
        gDriver.switch_to.window(gDriver.window_handles[1])
        gDriver.get('https://recconnect.bc.edu/booking/93a7d382-156f-472c-bf90-006fb897d1c4')
        element = gDriver.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
        actions = ActionChains(gDriver)
        actions.move_to_element(element).perform()
        element.click()
        day = gDriver.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]').get_attribute("data-day")
        day = int(day)
        time.sleep(1)
        gDriver.close()
        gDriver.switch_to.window(gDriver.window_handles[0])
        return(day)
    
    day = check_date()
    
    
    while initial_day == day:
        try:
            print(datetime.now())
            print('New gym appointments not yet available.')
            print('Rechecking...')
            time.sleep(1)
            day = check_date()


        except:
            print('Rechecking...')
            time.sleep(1)
            try:
                day = check_date()
            except:
                print('ERROR, please restart!')
                
    #Book Appointment
    if (datetime.today().strftime('%A') == 'Monday') or (datetime.today().strftime('%A') == 'Sunday') or (datetime.today().strftime('%A') == 'Saturday') or (datetime.today().strftime('%A') == 'Friday'):
        browser.get('https://recconnect.bc.edu/booking/93a7d382-156f-472c-bf90-006fb897d1c4')
        element = browser.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        element.click()

        last_book = browser.find_element_by_css_selector ('#divBookingSlots > div > div:nth-child(9) > div > button')
        actions = ActionChains(browser)
        actions.move_to_element(last_book).perform()
        browser.find_element_by_css_selector  ('#divBookingSlots > div > div:nth-child(1) > div > button')
    
        

            
        

                
    #Book Appointment
    if (datetime.today().strftime('%A') == 'Monday') or (datetime.today().strftime('%A') == 'Sunday') or (datetime.today().strftime('%A') == 'Saturday') or (datetime.today().strftime('%A') == 'Friday'):
        browser.get('https://recconnect.bc.edu/booking/93a7d382-156f-472c-bf90-006fb897d1c4')
        element = browser.find_element_by_xpath ('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
        actions = ActionChains(browser)
        actions.move_to_element(element).perform()
        element.click()

        last_book = browser.find_element_by_css_selector ('#divBookingSlots > div > div:nth-child(9) > div > button')
        actions = ActionChains(browser)
        actions.move_to_element(last_book).perform()
        browser.find_element_by_css_selector  ('#divBookingSlots > div > div:nth-child(1) > div > button')
    
        

            
        
        


# In[ ]:


try:
    book()
except:
    book()


# In[ ]:





# In[ ]:




