from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def loginfunction(un, up):
    
    time.sleep(5)
    usernametb = config.driver.find_element_by_xpath('//*[@id="loginemail"]').send_keys(un)
    time.sleep(5)
    passwordtb = config.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(up)
    time.sleep(3)
    loginbtn = config.driver.find_element_by_xpath('//*[@id="mhLP-ln"]/div[2]/form/div[6]/button')
    loginbtn.click() 
    time.sleep(5)
    
def clicktabsfunction():
    
    time.sleep(3)
    PatientMngr = config.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[3]')
    PatientMngr.click()
    time.sleep(5)
    patient = config.driver.find_element_by_xpath('//*[@id="sidebar"]/side-bar/div/div[1]/ul/li[3]/ul/li[1]/a')
    patient.click()
    time.sleep(5)
    pageFind = config.driver.find_element_by_xpath('//*[@id="data-table-command-footer"]/div/div[1]/ul/li[4]')
    pageFind.click()
    time.sleep(5)
    patientName = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[3]')
    patientName.click()
    time.sleep(5)
    
def editOasisfunction(comm):
    
    openOasis = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')
    openOasis.click()
    time.sleep(5)
    Xbtn = config.driver.find_element_by_xpath('//*[@id="closecomments"]')
    Xbtn.click()
    time.sleep(5)
    X2btn = config.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    EditOasisbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button')
    EditOasisbtn.click()
    time.sleep(5)
    chooseSection = config.driver.find_element_by_xpath('//*[@id="integumentary"]/div')
    chooseSection.click()
    time.sleep(5)
    checkboxWound = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/label/input')
    checkboxWound.click()
    time.sleep(5)
    addLabelwound = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/a')
    addLabelwound.click()
    time.sleep(5)
    Woundmenu = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[1]/input')
    Woundmenu.click()
    time.sleep(5)
    selectWoundType = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[2]/ul/li[9]')
    selectWoundType.click()
    time.sleep(5)
    location = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[1]/input')
    location.click()
    time.sleep(5)
    selectLocation = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[2]/ul/li[3]')
    selectLocation.click()
    time.sleep(5)
    commenttb = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[7]/input').send_keys(comm)
    time.sleep(5)
    X2btn = config.driver.find_element_by_xpath('/html/body/div[11]/button')
    X2btn.click()
    time.sleep(5)
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button[3]')
    savebtn.click()
    time.sleep(5)
    assessbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    assessbtn.click()
    time.sleep(5)

def woundcareFunction():
    
    degree = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input')
    degree.click()
    time.sleep(5)
    selectDegree = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]/span/table-inputs/div/div[2]/ul/li[2]')
    selectDegree.click()
    time.sleep(5)
    amount = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input')
    amount.click()
    time.sleep(5)
    selectAmount = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]/span/table-inputs/div/div[2]/ul/li[6]')
    selectAmount.click()
    time.sleep(5)
    Type = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[1]/input')
    Type.click()
    time.sleep(5)
    selectType = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]/span/table-inputs/div/div[2]/ul/li[6]')
    selectType.click()
    time.sleep(5)
    Status = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[1]/input')
    Status.click()
    time.sleep(5)
    selectStatus = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]/span/table-inputs/div/div[2]/ul/li[6]')
    selectStatus.click()
    time.sleep(5)
    RelatedPain = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[1]/input')
    RelatedPain.click()
    time.sleep(5)
    selectScore = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]/span/table-inputs/div/div[2]/ul/li[7]')
    selectScore.click()
    time.sleep(5)
    upload = config.driver.find_element(By.XPATH, '//*[@id="myImg"]')
    upload.send_keys('C:/Users/USER/Desktop/ORIGINAL IMAGE/wound-images-week_6')
    
    