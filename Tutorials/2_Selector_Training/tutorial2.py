from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

HOME_URL = "https://www.reutlingen-university.de/"
EVENTS_PATH = "/aktuelles/veranstaltungen-und-termine"


def handle_cookie_banner(driver):
    """
    Minimal helper: close cookie banner if present.
    """
    wait = WebDriverWait(driver, 5)
    try:
        btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Auswahl erlauben') or contains(., 'Akzeptieren')]")
            )
        )
        btn.click()
        print("Cookie-Banner geschlossen.")
    except TimeoutException:
        print("Kein Cookie-Banner gefunden / schon weg.")


def tutorial2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(HOME_URL)
        handle_cookie_banner(driver)

        # Auf Bachelor drücken
        # Variante mit Link-Text
        
        
        # TODO: Live Coding
        # Zuerst Bachelor anklicken, Back, dann Master anklicken
        # Am ende noch Variante mit wait.until zeigen
        
        
        # andere Variante: mit CSS-Selector ()
        # Auf Master drücken
        
        # TODO: Live Coding
        

    finally:
        driver.quit()


if __name__ == "__main__":
    tutorial2()
