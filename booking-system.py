import threading
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

phone_numbers = [6133142900, 6138826678]
emails = ["hochunglai@gmail.com", "chanyo99@hotmail.com"]
names = ["Deryck Ho", "Yoyo Chan"]


def start_threads():
    threads = []
    start_time = time.time()
    for i in range(2):
        thread = threading.Thread(target=book, args=(
            i, phone_numbers[i], emails[i], names[i]))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


def book(num, phone_num, email, name):

    print(f"Worker {num} {phone_num} {email} {name} started")

    chrome_options = Options()

    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        (ChromeDriverManager().install()), chrome_options=chrome_options)

    driver.get("https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000")

    sport = driver.find_element_by_xpath(
        "//div[@class='content' and text()='Squash - court 2']")
    sport.click()

    try:
        # Number of People
        num_people_input = driver.find_element_by_name("ReservationCount")
        num_people_input.clear()
        num_people_input.send_keys("2")

        confirm_button = driver.find_element_by_id("submit-btn")
        confirm_button.click()
    except:
        print("\n\n\n\n\nNo need to enter number of people\n\n\n\n\n")

    # Expend Date List
    while True:
        try:
            date_button = driver.find_element_by_xpath(
                '//*[@id="mainForm"]/div[2]/div[2]/a')
            date_button.click()
        except:
            driver.refresh()
            continue
        break

    # Choose time
    elements = driver.find_elements(By.XPATH, f"//a[@aria-label]")
    for element in elements:
        try:
            element.click()
        except:
            print(f"{num} {element.text} Failed")
            continue

    # Phone number
    phone_number_input = driver.find_element_by_name("PhoneNumber")
    phone_number_input.send_keys(phone_num)

    # Email
    email_input = driver.find_element_by_name("Email")
    email_input.send_keys(email)

    # Name
    name_input = driver.find_element_by_xpath('//input[@type="text"]')
    name_input.send_keys(name)

    confirm_button = driver.find_element_by_id("submit-btn")
    # confirm_button.click()

    confirm_button = driver.find_element_by_id("submit-btn")
    # confirm_button.click()

    driver.quit()

    print(f"Worker {num} finished")


start_threads()
