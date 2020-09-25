from .login import Login
from .common.utils.login import login
from .common.utils.race import wait_to_load, is_qualifying
from .race import NormalRace, QualifyingRace
import time


class NitroType:
    def __init__(self, driver, login: Login):
        self.driver = driver
        self.login_ = login

        self.driver.get("https://www.nitrotype.com")

    def login(self):
        if self.login_.guest:
            pass

        else:
            login(self.driver, self.login_)

    def race(self):
        """
        Starts a race, but also waits for it to load,
         and either gives back a NormalRace() object, or QualifyingRace() object.
        :return:
        """
        self.driver.get("https://www.nitrotype.com/race")
        wait_to_load(self.driver)
        time.sleep(0.8)
        if is_qualifying(self.driver):
            return QualifyingRace(self.driver)

        else:
            return NormalRace(self.driver)
