
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

class IgBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        # Put your geckodriver path here #
        self.driver = webdriver.Firefox(executable_path=r'C:\***put_the_path_here***\geckodriver.exe') 

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(2)
        try:
            login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print('\n','Log in...','\n')
        
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(2, 3))
        user_element.send_keys(self.username)
        time.sleep(random.randint(2, 4))
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(2, 4))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(3, 4))
        
        time.sleep(2)
        
        self.driver.get("https://www.instagram.com/{}/".format(self.username))
        time.sleep(3)
        
        self.get_unfollowers()
                   
    def followers(self):
        last_scrl, scrol = 0, 1
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers/')]").click()
        time.sleep(3)
        
        print("Searching...","\n")
     
        while last_scrl != scrol:
        
            scrl = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            
            followers =  self.driver.find_elements_by_class_name("FPmhX")
            followers = [elem.get_attribute("title") for elem in followers]
            
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrl)
            time.sleep(round(random.uniform(0.75, 1.0), 1))            
            
            last_scrl = scrol  
            scrol = len(followers)
        
        # aria-label changes according to the language #   
        self.driver.find_element_by_css_selector("[aria-label='Fechar']").click()
             
        return followers
    
    def get_unfollowers(self):     
        followers = self.followers()
        last_scrl, scrol = 0, 1
        self.driver.find_element_by_xpath("//a[contains(@href,'/following/')]").click()
        time.sleep(3)
        
        while last_scrl != scrol:
            
            scrl = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            
            following =  self.driver.find_elements_by_class_name("FPmhX")
            following = [elem.get_attribute("title") for elem in following]
            
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrl)
            time.sleep(round(random.uniform(0.75, 1.0), 1))  
            
            last_scrl = scrol  
            scrol = len(following)

        self.driver.find_element_by_css_selector("[aria-label='Fechar']").click()
        
        unfollowers = [user for user in following if user not in followers]
        
        
        print("These are the unfollowers that you are following.","\n")
        for i in range(len(unfollowers)):
            print(i+1, unfollowers[i])
      
# Put your login and password here #
ig_bot = IgBot('your_login','your_password')
ig_bot.login()
