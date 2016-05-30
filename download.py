import os
import shutil
import time
import sys
from selenium import webdriver
#====================================================
site = "http://www.youtube-mp3.org/" #do not change
searchBox = "youtube-url" #do not change
searchButton = "submit" #do not change
downButton = ".//*[@id='dl_link']/a[3]/b"
youtube = str(sys.argv[1])
#====================================================
def downloadMusic(url):
    browser = webdriver.Firefox()
    browser.get(site)
    search = browser.find_element_by_id(searchBox)
    search.clear()
    search.send_keys(url)

    submit = browser.find_element_by_id(searchButton)
    submit.click()

    #Do not comment out the call before, see below for explanation
    # checkIfReady(browser, downButton)

    return

downloadMusic(youtube)

#==========================================
#ignore the function below until further notice
#I have to configure webdriver settings to allow for a download to occur without an alert window "confirming it". Current settings prompt an alert window which make the user go in and manually close it
# def checkIfReady(driver, selector):
#     isPresent = driver.find_elements_by_xpath(selector)
#     if len(isPresent) == 0:
#         print (len(isPresent))
#         checkIfReady(driver, selector)
#     else:
#         print ("its there============")
#         time.sleep(7)
#         driver.find_element_by_xpath(selector).click()
#     return
