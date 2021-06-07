from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import function
import config
#import Upload


config.driver.get("https://qado.medisource.com/login")
config.driver.maximize_window()

function.loginfunction('superagent@geeksnest', 'Tester2021@')
function.clicktabsfunction()
function.editOasisfunction('Lorem Ipsum')
function.woundcareFunction()
#Upload.uploaderfunction()
#function.UploadImgfunction()





