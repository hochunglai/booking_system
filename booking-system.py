#!/usr/bin/env python3

import threading
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

phone_numbers = [6133142900, 6138826678]
emails = ["hochunglai@gmail.com", "chanyo99@hotmail.com"]
names = ["Deryck Ho", "Yoyo Chan"]
sessions = ["8:00", "9:15"]


def start_threads():

    threads = []
    for i in range(2):
        for j in range(2):
            thread = threading.Thread(target=book, args=(
                i, full_time_format(sessions[j]), phone_numbers[i], emails[i], names[i]))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


def book(num, session, phone_num, email, name):

    print(f"Worker {num} {phone_num} {email} {name} started")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        (ChromeDriverManager().install()), chrome_options=chrome_options)

    driver.get("https://reservation.frontdesksuite.ca/rcfs/nepeansportsplex/Home/Index?Culture=en&PageId=b0d362a1-ba36-42ae-b1e0-feefaf43fe4c&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000")

    sport = driver.find_element(By.XPATH,
                                "//div[@class='content' and text()='Badminton']")
    sport.click()

    try:
        # Number of People
        num_people_input = driver.find_element(By.NAME, "ReservationCount")
        num_people_input.clear()
        num_people_input.send_keys("2")

        confirm_button = driver.find_element(By.ID, "submit-btn")
        confirm_button.click()
    except:
        print("\n\n\n\n\nNo need to enter number of people\n\n\n\n\n")

    # Expend Date List
    while True:
        try:
            date_button = driver.find_element(By.XPATH,
                                              f"//*[contains(text(), '{time_format()}')]")
            date_button.click()
        except:
            driver.refresh()
            continue
        break

    # Choose time
    driver.find_element(By.XPATH, f"//a[@aria-label='{session}']").click()

    # Phone number
    driver.find_element(By.ID, 'telephone').send_keys(phone_num)

    # Email
    driver.find_element(By.NAME, 'Email').send_keys(email)

    # Name
    driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(name)

    driver.find_element(By.ID, "submit-btn").click()

    driver.find_element(By.ID, "submit-btn").click()

    input()
    driver.quit()


def full_time_format(session):
    today = datetime.date.today()

    # Add 2 days to today's date
    dt = today + datetime.timedelta(days=2)

    formatted_date = session + dt.strftime(" %p %A %B %-d, %Y")
    print("\n\n"+formatted_date+"\n\n")
    return formatted_date


def time_format():
    today = datetime.date.today()

    # Add 2 days to today's date
    dt = today + datetime.timedelta(days=2)

    formatted_date = dt.strftime("%A %B %-d, %Y")
    print("\n\n"+formatted_date+"\n\n")
    return formatted_date


start_threads()
