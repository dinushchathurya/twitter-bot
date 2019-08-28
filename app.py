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

    #Login method
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        #Pause your app for 3 seconds
        time.sleep(3)
        email = bot.find_element_by_class_name ('email-input')
        password = bot.find_element_by_class_name('session [password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        #Auto click on the login button
        password.send_keys(keys.RETURN)
        time.sleep(3)
    
    #Create function to like all the tweets which include specified hashtag
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
    #Create instance of TwitterBot class
    ed = TwitterBot('your email' , 'your password')
    #Call the login function
    ed.login()



