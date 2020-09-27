from selenium import webdriver
from nitrotypelib import NitroType
from nitrotypelib.login import Login
from nitrotypelib.common.utils.race import start_race
from nitrotypelib.login.login import create_account


driver = webdriver.Firefox()
login = Login(False, "username", "password")

session = NitroType(driver, login)
create_account(driver, login)

race = session.race()

text, input_area = start_race(race)

for letter in text:
    input_area.send_keys(letter)
