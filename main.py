import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook, load_workbook
from dotenv import load_dotenv
import os
import time

def calenderScrape():
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    load_dotenv()
    
    url = "https://estudijas.rtu.lv/"
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button").click()
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/form/input")
    elem.send_keys(os.getenv("USER"))
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/form/input")
    elem.send_keys(os.getenv("PASS"))
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[3]/td[2]/input").click()
    time.sleep(1)
    if driver.title == "ORTUS (Neveiksmīga autentifikācija)":
        print("Invalid login info. Try again")
    
    


if __name__ == "__main__":
    calenderScrape()