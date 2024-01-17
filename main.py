from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
from dotenv import load_dotenv, set_key
import getpass
import os
import time

def calenderScrape():
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    actions = ActionChains(driver)
    load_dotenv("info.env")
    
    url = "https://estudijas.rtu.lv/"
    driver.get(url)
    driver.find_element(By.XPATH, "/html/body/div[3]/header[1]/div/div/div[2]/div/form/div[1]/button").click()
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[1]/td[2]/form/input")
    elem.send_keys(os.getenv("USER"))
    elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[2]/td[2]/form/input")
    elem.send_keys(os.getenv("PASS"))
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr[3]/td[2]/input").click()
    time.sleep(1)
    if driver.title == "ORTUS (Neveiksmīga autentifikācija)":
        driver.quit()
        updateKeys()
    
    eventNames = []
    eventTimes = []
    events = driver.find_elements(By.CSS_SELECTOR, "h6.d-flex.mb-1")

    for val in events:
        val = val.text
        val = val.splitlines()
        try:
            eventNames.append(val[0])
            eventTimes.append(val[1])
        except IndexError:
            pass
    tableGen(eventNames, eventTimes)

def tableGen(eventNames, eventTimes):
    wb = openpyxl.Workbook()
    wb.save("planned_events.xlsx")
    ws = wb.get_sheet_by_name("Sheet1")
    
    ws["A1"]="Event name"
    ws["B1"]="End date"
    ws["C1"]="Time left"
    row=2
    i=0
    for val in eventNames:
        ws[f"A{row}"] = val
        ws[f"B{row}"] = eventTimes[i]
        ws[f"C{row}"] = "="


def updateKeys():
    print("Invalid login info. Update .env file keys.")
    os.environ["USER"] = input("Enter new ORTUS username: ")
    os.environ["PASS"] = getpass.getpass("Enter new ORTUS password: ")
    set_key("info.env", "USER", os.environ["USER"])
    set_key("info.env", "PASS", os.environ["PASS"])
    print("Keys updated.")
    calenderScrape()

if __name__ == "__main__":
    calenderScrape()