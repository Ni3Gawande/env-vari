from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import pytest

def test_login():
        load_dotenv()
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Make Appointment'])[1]"))).click()
        username = wait.until(EC.element_to_be_clickable((By.ID, "txt-username")))
        username.click()
        username.send_keys(os.getenv("name"))
        passw = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='txt-password']")))
        passw.click()
        passw.send_keys(os.getenv("password"))
        wait.until(EC.element_to_be_clickable((By.ID, "btn-login"))).click()
        title=driver.title
        print(title)
        assert title == "CURA Healthcare Service"
        driver.close()
