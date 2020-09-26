from selenium import webdriver
from nitrotypelib import NitroType
from nitrotypelib.login import Login
from bot import bot
import random
import time


def decide_if_win():
    return random.choice([True, False, False])


def main():
    session, driver, login = startup()
    while True:
        race = session.race()
        going_to_win = decide_if_win()
        print(f"Going to win: {going_to_win}")
        bot(driver, race, session, login, going_to_win)
        time.sleep(3)


def startup():
    driver = webdriver.Firefox()
    login = Login(False, "trulyfresh6", "minecraft")

    session = NitroType(driver, login)
    session.login()
    time.sleep(0.2)

    return session, driver, login


if __name__ == '__main__':
    main()
