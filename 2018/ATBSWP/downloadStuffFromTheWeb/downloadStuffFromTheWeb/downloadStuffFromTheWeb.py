import requests
import urllib3
import json
import bs4
import selenium
from selenium import webdriver

browser = webdriver.Firefox()

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\program files (x86)\microsoft visual studio\shared\python36_64\lib\site-packages\selenium\webdriver\firefox\firefox_binary.py')
browser = webdriver.Firefox(firefox_binary=binary)