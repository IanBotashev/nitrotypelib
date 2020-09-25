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
