from selenium import webdriver
from nitrotypelib import NitroType
from nitrotypelib.login import Login
from nitrotypelib.common.utils.race import start_race


driver = webdriver.Firefox()
login = Login(True, "trulyfresh6", "minecraft")

session = NitroType(driver, login)
session.login()

race = session.race()

text, input_area = start_race(race)