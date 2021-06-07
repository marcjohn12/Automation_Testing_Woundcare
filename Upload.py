from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


def uploaderfunction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://qado.medisource.com/patientcare/EE6B3991-4CC5-4E4B-A3E9-71CA82BA54CC/4654B296-A29A-47FF-BAF2-7F4317844797/woundcare/list')
    element = driver.find_element(By.XPATH, '//*[@id="myImg"]')
    element.send_keys("C:/Users/USER/Desktop/ORIGINAL IMAGE/wound-images-week_6")

