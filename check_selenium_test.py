from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = "https://www.reutlingen-university.de/"
        print(f"Öffne {url} ...")
        driver.get(url)

        page_title = driver.title
        print(f"Seitentitel: {page_title!r}")

        assert "Reutlingen" in page_title

        h1 = driver.find_element(By.TAG_NAME, "h1")
        print(f"H1-Text: {h1.text!r}")

        print("Selenium-Setup scheint zu funktionieren!")
    except Exception as e:
        print("Es ist ein Fehler aufgetreten. Bitte Screenshot machen und im Workshop mitbringen.")
        print(f"Fehler: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
