from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from nitrotypelib.race import TR_QUALIFY, TR_NORMAL
import time


def is_qualifying(driver):
    """
    Tests to see if the current race is a Qualifying Race
    :return:
    """
    try:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/div/section/div[3]/div[1]/div[1]/div[3]/div/button")
        return True

    except NoSuchElementException:
        return False


def wait_to_load(driver, delay=5):
    """
    Waits until the race page loads in.
    Sadly, still is a bit inaccurate, sometimes by just a couple of milliseconds.
    :return:
    """
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "raceLight")))
    time.sleep(1)


def start_race(race):
    """
    Starts the race, or waits for the race to start,
    and also waits for text.
    :return:
    """
    print(race.race_type)
    if race.race_type == TR_QUALIFY:
        race.start_race()

    race.wait_for_start()
    text, input_area = race.get_data()

    return text, input_area
