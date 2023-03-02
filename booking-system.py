from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome((ChromeDriverManager().install()), chrome_options=chrome_options)

driver.get("https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000")
badminton_button = driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div[15]/div[4]/a")
badminton_button.click()

try:
    #Number of People
    num_people_input = driver.find_element_by_name("ReservationCount")
    num_people_input.clear()
    num_people_input.send_keys("2")

    confirm_button = driver.find_element_by_id("submit-btn")
    confirm_button.click()
except:
  print("\n\n\n\n\nNo need to enter number of people\n\n\n\n\n")

# Expend Date List
date_button = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[3]/a')
date_button.click()

#Choose time 
span_button = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[3]/ul/li[13]/a')
span_button.click()

#Phone number
phone_number_input = driver.find_element_by_name("PhoneNumber")
phone_number_input.send_keys("6133142900")

#Email
email_input = driver.find_element_by_name("Email")
email_input.send_keys("hochunglai@gmail.com")

#Name
name_input = driver.find_element_by_xpath('//input[@type="text"]')
name_input.send_keys("Deryck")

confirm_button = driver.find_element_by_id("submit-btn")
confirm_button.click()

confirm_button = driver.find_element_by_id("submit-btn")
confirm_button.click()

input("")
print("OK")

driver.quit()




