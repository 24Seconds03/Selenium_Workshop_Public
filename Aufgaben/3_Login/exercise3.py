from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def handle_cookie_banner(driver):
    """Hilfsfunktion: Cookie-Banner wegklicken (gegeben, bitte nicht ändern)."""
    wait = WebDriverWait(driver, 5)
    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Auswahl erlauben')]")
            )
        )
        cookie_button.click()
    except TimeoutException:
        pass


def click_and_follow(driver, element, timeout: int = 15):
    """
    Hilfsfunktion (gegeben):
    - klickt auf ein Element
    - falls ein neues Tab/Fenster entsteht, wird dorthin gewechselt
    - gibt die aktuelle URL zurück
    """
    wait = WebDriverWait(driver, timeout)

    original_windows = driver.window_handles[:]
    element.click()

    # Falls ein neues Fenster dazukommt → wechseln
    if len(driver.window_handles) > len(original_windows):
        new_window = [h for h in driver.window_handles if h not in original_windows][0]
        print("Neues Fenster/Tab gefunden, wechsle dorthin ...")
        driver.switch_to.window(new_window)

    # Optional: kurze Wartebedingung, z.B. bis die URL sich geändert hat
    wait.until(lambda d: d.current_url != "")
    print(f"Aktuelle URL nach Klick: {driver.current_url}")
    return driver.current_url


def exercise_login():
    """
    Übung 3: Login
    
    Ziel: 
    - Auf der Startseite den Login-Link finden und klicken
    - Auf der Login-Seite prüfen, ob wir richtig gelandet sind
    - Den HISinOne finden und klicken
    - Auf der HISinOneSeite Benutzername und Passwort eingeben
    - Den Login-Button klicken
    - (Optional) Prüfen, ob der Login erfolgreich war (z.B. durch Suche nach einem bestimmten Element)
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.reutlingen-university.de/")
        wait = WebDriverWait(driver, 10)

        handle_cookie_banner(driver)

        # TODO 1:
        # Auf Login button drücken
                
        # TODO 2:
        # checken, ob wir auf der richtigen Webseite sind
        # z.B. den Text 'Schon eingeloggt?' untersuchen
        
        # TODO 3:
        # HISinOne Link (HisinOne (Campusportal für Bewerber:innen & studierende)) finden und klicken
        # ggf. die Funktion click_and_follow und anschließend handle_cookie_banner verwenden    
        
        
        # TODO 4:
        # Benutzername und Passwort eingeben und Login-Button klicken
        # Tipp: By.NAME oder By.ID ist hier hilfreich
        
        # TODO 5 (Optional):
        # Prüfen, ob der Login erfolgreich war
        
        print("✅ Übung 3: Wenn ihr bis hier ohne Fehler kommt, habt ihr euren eigenen Flow gebaut.")

    finally:
        driver.quit()


if __name__ == "__main__":
    exercise_login()
