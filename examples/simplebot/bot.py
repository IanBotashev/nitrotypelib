from nitrotypelib.race import TR_QUALIFY
from nitrotypelib.common.utils.race import start_race
import time


def decide_wpm(race, username, default_wpm, current_wpm, going_to_win):
    wpm = current_wpm

    if going_to_win:
        if race.check_leader() != username:
            wpm = wpm + default_wpm/4

        else:
            wpm = default_wpm

    else:
        if race.check_leader() == username:
            wpm = wpm - default_wpm/4

        else:
            wpm = default_wpm

    return wpm


def calculate_time(wpm):
    """
    Calculates the times between
    :param wpm:
    :return:
    """
    return 1/(wpm/60*5)


def typing(driver, username, race, default_wpm, going_to_win, text, input_area, decide_next_wpm=True):
    wpm = default_wpm
    for letter in text:
        input_area.send_keys(letter)

        if decide_next_wpm:
            wpm = decide_wpm(race, username, default_wpm, wpm, going_to_win)

        time.sleep(calculate_time(wpm))


def bot(driver, race, session, login, going_to_win, default_wpm: int =180):
    """
    The bot.
    :param driver:
    :param race:
    :param session:
    :param login:
    :param going_to_win:
    :param default_wpm:
    :return:
    """
    text, input_area = start_race(race)
    if race.race_type == TR_QUALIFY:
        decide_next_wpm = False

    else:
        decide_next_wpm = True

    typing(driver, login.username, race, default_wpm, going_to_win, text, input_area, decide_next_wpm)
