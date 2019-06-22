from selenium import webdriver
import os

application_url = "localhost:5000"
driver_path = "/Users/kiril/Downloads/chromedriver_75"


def test_score_service():
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(application_url)
    score = int(driver.find_element_by_id("score").text)

    if score >= 1 and score <= 1000:
        return True
    else:
        return False


def main_function():
    if test_score_service():
            exit(0)
    else:
        exit(-1)



