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


def exercise_language_switcher():
    """
    Übung 4: Sprachumschalter Test (Optional)
    
    Ziel: UI-Test für Internationalisierung (EN-Button)
    
    Vorgehen:
    1. Stelle sicher, dass du auf der deutschen Version bist (ggf. /de aktiv)
    2. Klicke auf Englisch im Header
    3. Prüfe: URL wechselt von / auf z.B. /en oder ähnliches
    4. Der Haupttitel oder bestimmte Texte sind englisch 
       (z.B. "Reutlingen University" statt "Hochschule Reutlingen")
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.reutlingen-university.de/")
        wait = WebDriverWait(driver, 10)

        handle_cookie_banner(driver)

        # TODO 1:
        # Stelle sicher, dass du auf der deutschen Version bist
        # Falls die URL /en enthält, wechsle zu /de
        # Prüfe, dass wir auf der deutschen Version sind (z.B. durch URL-Check oder Text-Prüfung)
        

        # TODO 2:
        # Englisch-Button im Header finden
        # Hinweis: Nutzt DevTools, um den Sprachumschalter zu finden
        # Mögliche Selektoren: By.LINK_TEXT("EN"), By.PARTIAL_LINK_TEXT("EN"), 
        #                     By.CSS_SELECTOR("a[href*='/en']"), etc.
        

        # TODO 3:
        # Auf Englisch-Button klicken
        # Warten, bis die Seite neu geladen wurde
        # Speichere die URL vor dem Klick, um sie später zu vergleichen
        

        # TODO 4:
        # Prüfe: URL wechselt von / auf z.B. /en oder ähnliches
        # Prüfe verschiedene mögliche URL-Muster (/en, lang=en, etc.)
        

        # TODO 5:
        # Prüfe, dass bestimmte Texte jetzt englisch sind
        # z.B. "Reutlingen University" statt "Hochschule Reutlingen"
        # Prüfe Haupttitel (H1) oder andere charakteristische Texte
        # Hinweis: Suche nach englischen Indikatoren im Seitentitel, H1 oder Body-Text
        

        print("✅ Übung 4: Sprachumschalter erfolgreich getestet.")

    finally:
        driver.quit()


if __name__ == "__main__":
    exercise_language_switcher()

