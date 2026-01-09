from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time


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


def extract_events_from_page(driver):
    """
    Extrahiert alle Events von der aktuellen Seite.
    Gibt eine Liste von Dictionaries zurück mit: Datum/Uhrzeit, Titel, Detail-Link
    
    TODO: Implementiere diese Funktion
    - Finde alle div.teaser-text Container (jeder ist ein einzelnes Event)
    - Für jeden Container:
      - Extrahiere Datum/Uhrzeit aus time.teaser-text__date span
      - Extrahiere Titel aus h4.teaser-text__title
      - Extrahiere Detail-Link aus div.teaser-text__link a
      - Stelle sicher, dass relative Links zu vollständigen URLs werden
    - Vermeide Duplikate (z.B. durch Set von Links)
    """
    events = []
    
    # TODO: Implementiere die Event-Extraktion
    
    return events


def exercise_events_csv():
    """
    Übung 5: Events sammeln & als CSV speichern (Optional)
    
    Ziel: Exercise 2 erweitern, auf der Events-Seite alle sichtbaren Events 
    aus der Teaser-Liste einsammeln:
    - Datum / Uhrzeit
    - Titel (h4)
    - Detail-Link
    
    Seite 1 und 2 durchgehen und Ergebnisse als events.csv speichern
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    all_events = []
    
    try:
        driver.get("https://www.reutlingen-university.de/")
        wait = WebDriverWait(driver, 10)

        handle_cookie_banner(driver)

        # TODO 1:
        # Zur Events-Seite navigieren (wie in Exercise 2)
        # Finde den Link zur Events-Seite und klicke darauf
        # Warte, bis die Events-Seite geladen ist
        

        # TODO 2:
        # Seite 1: Alle Events von der ersten Seite sammeln
        # Verwende die Funktion extract_events_from_page()
        # Füge die Events zu all_events hinzu
        

        # TODO 3:
        # Zur Seite 2 navigieren
        # Suche nach Pagination-Link (z.B. mit CSS-Selector für Seite 2)
        # Klicke auf den Pagination-Link
        # Warte, bis Seite 2 geladen ist (URL-Änderung oder Zeit warten)
        

        # TODO 4:
        # Seite 2: Alle Events von der zweiten Seite sammeln
        # Verwende wieder extract_events_from_page()
        # Füge die Events zu all_events hinzu
        

        # TODO 5:
        # Alle gesammelten Events als CSV speichern
        # Verwende csv.DictWriter mit den Spalten: 'datum_uhrzeit', 'titel', 'detail_link'
        # Speichere die Datei als 'events.csv'
        

        print("✅ Übung 5: Events erfolgreich gesammelt und gespeichert.")

    finally:
        driver.quit()


if __name__ == "__main__":
    exercise_events_csv()

