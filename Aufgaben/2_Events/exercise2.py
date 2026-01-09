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


def exercise_events():
    """
    Übung 2: Events-Seite testen (Listenansicht + Drilldown)

    Minimal (Pflicht):
    1) EVENTS_URL öffnen
    2) prüfen, dass die Seite plausibel geladen ist (Titel/H1/H2)
    3) Event-Detail-Links finden (mindestens 1)
    4) erstes Event öffnen 
    5) Detailseite prüfen:
       - H1 ist nicht leer
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.reutlingen-university.de/")
        wait = WebDriverWait(driver, 10)

        handle_cookie_banner(driver)

        # TODO 1:
        # Link zur Events-/Terminseite finden.
        # Nutzt DevTools, um herauszufinden, wie der Link auf der Startseite heißt.
        # Beispiele:
        #   By.LINK_TEXT, By.PARTIAL_LINK_TEXT oder ein CSS-Selector.
        

        # TODO 2:
        # Klickt auf den Events-Link
        
        
        # TODO 3:
        # überprüfen, dass wir auf der richtigen Seite sind
        # z.B. durch den Seitentitel oder eine Überschrift (h1/h2)
        
       
        # TODO 4:
        # Alle Links finden, die zu einer Event-Detail-Seite führen.
        # Hinweise:
        # - Nutzt DevTools an einem Event-Eintrag und untersucht den <a href="..."> Link
        # - Ihr könnt By.CSS_SELECTOR verwenden
        # anschließend überprüfen, ob mindestens ein Link gefunden wurde.
        

        # TODO 5:
        # auf den ersten Event-Link klicken und zur Detail-Seite wechseln
        # Dann h1-Text überprüfen (nicht leer)

        print("✅ Übung 2: done")

    finally:
        driver.quit()


if __name__ == "__main__":
    exercise_events()
