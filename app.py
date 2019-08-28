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
        far i in range (1,3):
          bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
          time.sleep(2)
          tweets = bot.find_element_by_class_name('tweet')
          links = [elem.get_attribute('data-permalink-path') for elem in tweets]
          for link in links:
              bot.get('https://twitter.com/' + link)
              try:
                  bot.find_element_by_class_name('HeartAnimation').click()
                  time.sleep(10)
              except Exception as ex:
                  time.sleep(60)
    
    #Create instance of TwitterBot class
    ed = TwitterBot('your email' , 'your password')
    #Call the login function
    ed.login()
    ed.like_tweet ('enter here the hashtag you need to like')
   



