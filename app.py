from selenium import webdriver
#Embedded key board
from selenium.webdriver.common.keys import keys
import time

#Create twitter bot class
class TwitterBot:
    #initialize the class
    def __init__(self,username,password):
    self.username = username
    self.password = password
    #Initialize the browser
    self.bot = webdriver.Firefox()



