import selenium


def find_available_achievements_section(driver):
    """
    Gets the sections where achievements are available.
    :param driver:
    :return:
    """
    result = driver.find_elements_by_class_name("notify--inline notify--brief")
    return result


def find_all_buttons(driver):
    """
    Selects all the achievement section buttons.
    :param driver:
    :return:
    """
    result = driver.find_elements_by_class_name("btn--thick")
    return result


def find_available_achievements(driver):
    """
    Finds all the available
    :param driver:
    :return:
    """
    result = driver.find_elements_by_class_name("btn--positive")
    return result


def get_achievement(driver, button):
    """
    Clicks an achievement, and removes the popup.
    :param driver:
    :param button:
    :return:
    """
    button.click()
    driver.find_elements_by_css_selector("button.btn--primary")


def get_all_achievements(driver, sections):
    """
    Goes into each section, and clicks on all available buttons.
    :param driver:
    :param sections:
    :return:
    """
    for section in sections:
        section.click()
        for button in find_available_achievements(driver):
            get_achievement(driver, button)
