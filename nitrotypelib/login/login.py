from .exceptions import CannotCreateAccount, LoginDenied
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def login(driver, login_data):
    """
    Logins the user in through the driver.
    :param driver:
    :param login_data:
    :return:
    """
    driver.get("https://www.nitrotype.com/login")
    driver.find_element_by_name("username").send_keys(login_data.username)
    driver.find_element_by_name("password").send_keys(login_data.password)

    driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/section/div[2]/div/div[3]/form/button").click()

    try:
        WebDriverWait(driver, 4).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".input-alert")))
        reason = driver.find_element_by_css_selector(".bucket-content").text
        raise LoginDenied(reason)
    except TimeoutException:
        pass


def create_account(driver, login_data):
    """
    Allows for creating new accounts
    :param driver:
    :param login_data:
    :return:
    """
    driver.get("https://www.nitrotype.com/signup")

    driver.find_element_by_name("username").send_keys(login_data.username)
    driver.find_element_by_name("password").send_keys(login_data.password)
    driver.find_element_by_name("email").send_keys(login_data.email)

    driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/section/div[2]/div[1]/div[3]/form/button").click()

    try:
        WebDriverWait(driver, 4).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".input-alert")))
        reason = driver.find_element_by_css_selector("div.bucket:nth-child(1) > div:nth-child(2)").text
        raise LoginDenied(reason)
    except TimeoutException:
        pass
