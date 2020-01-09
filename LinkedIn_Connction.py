import IPython
from selenium import webdriver 
import time
import parsel
import csv
import pickle

#Directing to webpage
driver = webdriver.Chrome('C:/Users/Akash/Downloads/chrome/chromedriver.exe')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#login to webpage.
#Getting user id from user
userId = input()
username1 = driver.find_elements_by_xpath("//*[@id='username']")
#print(type(username1[0]))
username1[0].send_keys(userId)

#getting password form user
passward = input()
passward1 = driver.find_elements_by_xpath("//*[@id='password']")
passward1[0].send_keys(passward)


#login click event.
log_in_button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
log_in_button.click()


#Find find keyword
keyskill = driver.find_element_by_xpath("//*[contains(@class,'search-global-typeahead__input always-show-placeholder')]")

print(keyskill)
keyskill.send_keys("java developer")

#Press the enter after sending the key
keyskill.send_keys(u'\ue007')

#search only people
time.sleep(5)
people = driver.find_element_by_xpath("//*[contains(@class,'search-vertical-filter__filter-item mr2')]")
print(people)
time.sleep(5)
people.click()
