import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

print(time.ctime())

#Setup
load_dotenv()
site_url = os.environ.get("URL2")

chrome_browser = webdriver.Chrome()
wait = WebDriverWait(chrome_browser, 10)

#Test Case
script_done = False
while not script_done:
    chrome_browser.get(site_url)

    #First name
    document_firstname = wait.until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )
    document_firstname.send_keys("James")
    time.sleep(1)

    #Last name
    document_lastname = chrome_browser.find_element(By.ID, "lastName")
    document_lastname.send_keys("Arthur")
    time.sleep(1)

    #Email
    document_email = chrome_browser.find_element(By.ID, "userEmail")
    document_email.send_keys("abcdef@gmail.com")
    time.sleep(1)

    #Gender
    gender = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Male"]'))
    )
    gender.click()
    time.sleep(1)

    #Phone Number
    phonenumber = chrome_browser.find_element(By.ID, "userNumber")
    phonenumber.send_keys("0123456789")
    time.sleep(1)

    #Date of Birth
    birth_date = wait.until(
        EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
        )
    birth_date.click()
    
    year_dropdown = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select"))
        )
    year_dropdown.send_keys("2001")
    
    month_dropdown = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select"))
        )
    month_dropdown.send_keys("January")
    
    day = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//div[contains(@class,"react-datepicker__day") '
            'and text()="1" '
            'and not(contains(@class,"outside-month"))]'
            ))
            )
    day.click()

    #Subjects
    subjects_input = wait.until(
        EC.presence_of_element_located((By.ID, "subjectsInput"))
    )
    subjects_input.send_keys("Computer Science")
    subjects_input.send_keys(Keys.ENTER)
    time.sleep(1)

    #Hobbies
    hobbies = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Sports"]'))
    )
    hobbies.click()
    time.sleep(1)

    #Upload Image
    upload_image = wait.until(
    EC.presence_of_element_located((By.ID, "uploadPicture"))
    )
    #Provide image directory
    upload_image.send_keys("/aaa/bbb/ccc/ddd/demo.png")

    #Address
    address = chrome_browser.find_element(By.ID, "currentAddress")
    address.send_keys("47 W 13th St, New York, NY 10011")
    time.sleep(1)

    #State
    state = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="state"]//input'))
    )
    state.send_keys("Haryana")
    state.send_keys(Keys.ENTER)
    time.sleep(1)

    #City
    city = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="city"]//input'))
    )
    city.send_keys("Panipat")
    city.send_keys(Keys.ENTER)
    time.sleep(1)

    script_done = True

    #Submission
    submit_button = chrome_browser.find_element(By.ID, "submit")
    submit_button.send_keys(Keys.ENTER)
    time.sleep(1)

    #Change to different page - Assertion
    wait.until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    time.sleep(1)

    #Close button
    close_button = wait.until(
    EC.element_to_be_clickable((By.ID, "closeLargeModal"))
    )
    close_button.click()
    time.sleep(1)

    #Refresh
    chrome_browser.refresh()
    time.sleep(2)

#Quit
chrome_browser.quit()
