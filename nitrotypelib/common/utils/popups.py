# This specific part of the code deals with closing popups which can appear in-between games
# such as Achievement popups.


def try_all_popups(driver):
    """
    Tries to remove all popups.
    :param driver:
    :return:
    """
    try:
        achievement_popups(driver)
    except:
        pass

    try:
        rank_up_popups(driver)
    except:
        pass


def achievement_popups(driver):
    """
    Removes achievement popups
    :param driver:
    :return:
    """
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/button").click()


def rank_up_popups(driver):
    """
    Removes rankup popups
    :param driver:
    :return:
    """
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div/div[1]/button").click()
