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
                (
                    By.XPATH,
                    "//button[contains(., 'Auswahl erlauben')]",
                )
            )
        )
        cookie_button.click()
    except TimeoutException:
        pass  # Kein Banner gefunden oder schon akzeptiert


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
    

def exercise_information_for():
    """
    Übung 1: 'Informationen für …' prüfen

    Ziel:
    - Links 'Studieninteressierte' und 'Studierende' im Abschnitt finden
    - Sichtbarkeit der Links prüfen
    - einen Link anklicken (z.B. 'Studieninteressierte')
    - auf der Zielseite eine sinnvolle Assertion machen (Titel / Überschrift / URL)
    """

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://www.reutlingen-university.de/")
        wait = WebDriverWait(driver, 10)

        handle_cookie_banner(driver)
        
        # TODO 1:
        # Link 'Studieninteressierte' finden.
        # Hinweis: By.LINK_TEXT kann hier helfen
        
        
        # TODO 2:
        # Link 'Studierende' 
        # Wieder: By.LINK_TEXT kann helfen
        
        
        # TODO 3:
        # Sichtbarkeit der Links prüfen.
        # Hinweis: .is_displayed()

        # Fügt hier eure Assertions ein.


        # TODO 4:
        # Klickt auf den Link 'Studieninteressierte' (oder 'Studierende') und
        # wartet, bis die Zielseite geladen ist.
        #
        # Vorschlag:
        #   click_and_follow Funktion verwenden
        #   danach:
        #       - auf Titel warten (z.B. EC.title_contains("Studieninteressierte"))
        #       - oder auf eine H1-Überschrift warten
        #

        # Implementiert:
        #   - Klick
        #   - sinnvolles wait

        # ---------------------------------------------------------
        click_and_follow(driver,TEMP_LINK) # TODO: ersetzt TEMP_LINK durch euren Link-Variable 
               

        print("✅ Übung 1: Wenn ihr bis hier ohne Fehler kommt, ist alles gut.")

    finally:
        driver.quit()


if __name__ == "__main__":
    exercise_information_for()
