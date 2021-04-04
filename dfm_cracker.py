import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random as rn 

def multiply(x,y):
    return x*y

def divide(x,y):
    return int(x/y)

def process_text(text):
    out = 0
    if "×" in text:
        text = text.strip("×")
        numbers = text.split()
        out = multiply(int(numbers[0]),int(numbers[-1]))
    if "÷" in text:
        text = text.strip("÷")
        numbers = text.split()
        out = divide(int(numbers[0]),int(numbers[-1]))
    return out


LOGSITE = "https://www.drfrostmaths.com/login.php?url=\%2Findex.php"
PASSWORD = "<YOUR PASSWORD HERE>"
PATH = "<PATH TO CHROMEDRIVER>//chromedriver.exe"
Q_SELECTOR = '#question'
username = "<YOUR USERNAME HERE>"

#css-selectors constants
user_selector = "#dfm-home-inner-content > form > input[type=text]:nth-child(1)"
pw_selector = "#dfm-home-inner-content > form > input[type=password]:nth-child(2)"
login_btn_selector = "#dfm-home-inner-content > form > input.very-large-button"
ans_selector = "#calculator-display"




optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
browser = webdriver.Chrome(PATH, options=optionss)
wait = WebDriverWait(browser, 10)

#code block to login on website and start a new game
browser.get(LOGSITE)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
Sel_user = browser.find_element_by_css_selector(user_selector) #Finds Selector
Sel_pas = browser.find_element_by_css_selector(pw_selector) #Finds Selector
enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
Sel_user.send_keys(username)
Sel_pas.send_keys(PASSWORD)
Sel_pas.send_keys(Keys.RETURN)
browser.back()
browser.get("https://www.drfrostmaths.com/timestables-game.php")

Sel_ans = browser.find_element_by_css_selector(ans_selector)

browser.find_element_by_class_name('very-large-button-variant').click()

#max is 69 otherwise system detect something is off
MAXPOINTS = 69

#loop to correctly enter question answer
for i in range(MAXPOINTS):
    randomwait = (rn.random())/2
    time.sleep(randomwait)
    question = browser.find_element_by_css_selector(Q_SELECTOR).text #Finds Selector
    ans = process_text(question)
    Sel_ans.send_keys(ans)
