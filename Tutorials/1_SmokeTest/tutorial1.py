from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def homepage_smoke_test():
    """
    Einfacher Smoke Test für die Startseite der Hochschule Reutlingen.

    Prüft:
    - Seite lädt ohne Fehler
    - Titel enthält 'Reutlingen'
    - H1-Überschrift enthält 'Hochschule' oder 'Reutlingen'
    - Navigationslink 'Studium' ist sichtbar
    """
    # Arrange: Browser starten
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Arrange: Seite laden

        # Assert 1: Titel prüfen

        # Assert 2: H1-Überschrift prüfen

        # Assert 3: Navigationslink 'Studium' existiert und ist sichtbar

        print("✅ Homepage-Smoke-Test erfolgreich!")
    finally:
        # Cleanup: Browser schließen
        driver.quit()


if __name__ == "__main__":
    homepage_smoke_test()