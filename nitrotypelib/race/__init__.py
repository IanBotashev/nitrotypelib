from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# Types of Races.
# Simply for the ease of access.
TR_NORMAL = "NORMAL"
TR_QUALIFY = "QUALIFY"


class Race:
    def __init__(self, driver):
        self.driver = driver

    def is_started(self):
        """
        Tests if the race has started.
        :return:
        """
        try:
            self.driver.find_element_by_class_name("raceLight")
            return False

        except NoSuchElementException:
            return True

    def get_input_area(self):
        """
        Gets the area where user input is put into.
        :return:
        """
        return self.driver.find_element_by_class_name("dash-copy-input")

    def get_text(self):
        """
        Gets text for the race.
        Also replaces u"\u00A0" with " " to save some poor developers time.
        :return:
        """
        return self.driver.find_element_by_class_name("dash-copy").get_attribute("textContent").replace(u"\u00A0", " ")

    def get_data(self):
        """
        Returns both get_text and get_input_area
        :return:
        """
        text = self.get_text()
        input_area = self.get_input_area()

        return text, input_area

    def wait_for_start(self, delay=100):
        try:
            WebDriverWait(self.driver, delay).until(ec.invisibility_of_element((By.CLASS_NAME, "raceLight")))
            return False
        except TimeoutException:
            return True


class NormalRace(Race):
    race_type = TR_NORMAL

    def check_leader(self):
        """
        Check who is leader.
        :param driver:
        :return:
        """
        try:
            leader = self.driver.find_element_by_class_name("racev3Map-poleLeader").text
        except NoSuchElementException:
            leader = True

        return leader


class QualifyingRace(Race):
    race_type = TR_QUALIFY

    def start_race(self):
        """
        Starts race.
        :return:
        """
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/div/section/div[3]/div[1]/div[1]/div[3]/div/button").click()
