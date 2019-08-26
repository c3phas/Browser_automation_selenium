#! /usr/bin/python3
#--Note: Github will only permit a few attempt you should use the API they provide
import os
import sys
import time
from selenium import webdriver
import argparse
#argparse will be used to correct the name of the repo to create
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--create", metavar="", required=True, help="Name of the repo to create")
args = parser.parse_args()
#the name of the repo will be stored in args.create
#Next we launch our browser
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window()

browser.get('http://github.com/login')
#browser.get('peter-macharia https://api.github.com/user')
#create a function that will handle our login and create a new repository
def create():
	#note we could have used find_element_by_id then using the inpect element to get the id of the item we want
	
	
	python_button = browser.find_elements_by_xpath('//*[@id="login_field"]')[0]
	python_button2 = browser.find_elements_by_xpath('//*[@id="password"]')[0]
	python_button_login = browser.find_elements_by_xpath('/html/body/div[3]/main/div/form/div[3]/input[7]')[0]
	python_button2.send_keys("mypassword")
	python_button.send_keys('myusername')
	python_button_login.click()
	python_new = browser.find_elements_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')[0]
	python_new.click()#click method will just on the button

	python_new_repo = browser.find_elements_by_xpath('//*[@id="repository_name"]')[0]
	python_new_repo.send_keys(args.create)
	python_new_repo.click()
	time.sleep(4)#wait for 4 seconds before proceeding
	python_create = browser.find_elements_by_xpath('/html/body/div[4]/main/div/form/div[3]/button')[0]
	python_create.click()
#we are done with the function
#Note you can do anything using this method ,the idea is the same
if __name__ == "__main__":
	create()
