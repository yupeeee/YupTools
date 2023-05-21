from typing import Any

import subprocess
import time

import pyperclip

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from .config import *


__all__ = [
    "ChromeDriver",
]


def load_driver() -> Chrome:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe '
                     r'--remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = Chrome(
        options=options,
        service=Service(ChromeDriverManager().install()),
    )

    return driver


class ChromeDriver:
    def __init__(
            self,
            time_to_wait: float = default_wait,
            time_to_sleep: float = default_sleep,
    ) -> None:
        self.time_to_wait = time_to_wait
        self.time_to_sleep = time_to_sleep

        self.driver = load_driver()

    def close_driver(
            self,
    ) -> None:
        self.driver.close()
        self.driver.quit()

    def wait(
            self,
    ) -> None:
        self.driver.implicitly_wait(self.time_to_wait)
        time.sleep(self.time_to_sleep)

    def go(
            self,
            url: str,
    ) -> None:
        self.driver.get(url)

        self.wait()

    def current_url(
            self,
    ) -> str:
        return str(self.driver.current_url)

    def get_element(
            self,
            find_element_by: str,
            element_value: str,
    ) -> Any:
        element = self.driver.find_element(
            by=getattr(By, find_element_by),
            value=element_value,
        )

        return element

    def get_elements(
            self,
            find_elements_by: str,
            elements_value: str,
    ) -> Any:
        elements = self.driver.find_elements(
            by=getattr(By, find_elements_by),
            value=elements_value,
        )

        return elements

    def does_element_exist(
            self,
            find_element_by: str,
            element_value: str,
    ) -> bool:
        try:
            self.driver.find_element(
                by=getattr(By, find_element_by),
                value=element_value,
            )

        except NoSuchElementException:
            return False

        return True

    def click(
            self,
            find_element_by: str,
            element_value: str,
    ) -> None:
        element = self.get_element(
            find_element_by=find_element_by,
            element_value=element_value,
        )

        element.click()

        self.wait()

    def input(
            self,
            find_element_by: str,
            element_value: str,
            input_value: str,
    ) -> None:
        element = self.get_element(
            find_element_by=find_element_by,
            element_value=element_value,
        )

        element.clear()

        element.click()
        pyperclip.copy(input_value)
        element.send_keys(Keys.CONTROL, "v")

        self.wait()

    def get_value(
            self,
            find_element_by: str,
            element_value: str,
            element_attribute: str,
    ) -> Any:
        element = self.get_element(
            find_element_by=find_element_by,
            element_value=element_value,
        )

        return element.get_attribute(element_attribute)

    def get_text(
            self,
            find_element_by: str,
            element_value: str,
    ) -> Any:
        element = self.get_element(
            find_element_by=find_element_by,
            element_value=element_value,
        )

        return element.text
