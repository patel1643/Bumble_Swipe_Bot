from selenium import webdriver
from time import sleep

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome("E:/University/tinderBot/Scripts/chromedriver.exe")
    def login(self):
        self.driver.get('https://bumble.com/')
    
        # sleep(7)
       
        login_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        login_btn.click()
        
        number_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[3]/div/span/span')
        number_btn.click()

        # # sleep(25)
        # # switch to login popup
        # # base_window = self.driver.window_handles[0]
        # # self.driver.switch_to_window(self.driver.window_handles[1])
    
        # # email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        # # email_in.send_keys('yourEmail')
    
        # # pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # # pw_in.send_keys('yourPassword')
    
        # # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        # # login_btn.click()
    
        # # self.driver.switch_to_window(base_window)
    
        # # popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # # popup_1.click()
    
        # # popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # # popup_2.click()
    
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            self.like()
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()    