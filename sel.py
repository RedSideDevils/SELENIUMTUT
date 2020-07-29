from selenium import webdriver
import time 

class person:

    def __init__(self):
        
        self.chromed = r''#webdriver path
        self.driver = webdriver.Chrome(self.chromed)

    def login(self, email, password):

        self.driver.get('https://mail.ru/?form=logout')
        self.driver.find_element_by_id('mailbox:login').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input').click()
        time.sleep(0.8)
        self.driver.find_element_by_id('mailbox:password').send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mailbox:submit"]/input').click()
        time.sleep(2)
        self.driver.get(self.driver.current_url)

    def send_message(self,to,subject,text):
        self.driver.get('https://e.mail.ru/compose/')
        time.sleep(2)
        self.driver.find_element_by_name('Subject').send_keys(subject)
        self.driver.find_elements_by_xpath('//input[@class="container--H9L5q size_s--3_M-_"]')[0].send_keys(to)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[1]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div[1]').send_keys(text)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//span[@class="button2 button2_base button2_primary button2_hover-support js-shortcut"]').click()


person = person()
person.login('botforselenium@mail.ru','potato228')
person.send_message('armenpilot2017@gmail.com','ITS WORKS', 'OMG IT"S WORKSSSSS')
