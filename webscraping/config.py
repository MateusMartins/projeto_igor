from selenium import webdriver
from selenium.webdriver.support.ui import Select

def get_driver():
    return webdriver.Firefox()