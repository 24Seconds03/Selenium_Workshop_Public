# Selenium Cheatsheet (Python) – Workshop

> Ziel: **so spezifisch wie nötig, so simpel wie möglich**  
> Faustregel Locator: **ID > stabile Klassen > Attribute > (zur Not) XPath**  
> Bevorzuge **Explicit Waits** statt `time.sleep()`.

---

## 0) Setup (Minimal)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

```python
driver = webdriver.Chrome()  # ggf. mit Service/Options je nach Setup
wait = WebDriverWait(driver, 10)

driver.get("https://www.reutlingen-university.de/")
```

**Nützlich:**
```python
driver.maximize_window()
driver.quit()
```

---

## 1) Browser & Navigation

```python
driver.get("https://www.reutlingen-university.de/")
driver.back()
driver.forward()
driver.refresh()

current_url = driver.current_url
title = driver.title
```

---

## 2) Developer Tools (zum Element finden)

- **Strg + Shift + I** → Developer Tools öffnen
- Im Tab **Elements**: HTML/DOM ansehen
- Im `<head>` findest du u.a. den `<title>`
- **Rechtsklick auf Element → „Untersuchen“** → springt direkt im DOM zur Stelle
- Optional: **Copy → Copy selector / Copy XPath** (als Startpunkt – oft noch vereinfachen!)

---

## 3) Elemente finden (Locators / `By.*`)

### Single Element
```python
h1 = driver.find_element(By.TAG_NAME, "h1")
nav = driver.find_element(By.LINK_TEXT, "Studium")
login = driver.find_element(By.ID, "login")        # Beispiel
search = driver.find_element(By.NAME, "q")         # Beispiel
```

### Multiple Elemente (`find_elements` → Liste, ggf. leer)
```python
links = driver.find_elements(By.TAG_NAME, "a")
buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn")
```

### Überblick `By`
- `By.ID`
- `By.NAME`
- `By.CLASS_NAME` (nur **eine** Klasse! Für mehrere → CSS verwenden)
- `By.TAG_NAME`
- `By.LINK_TEXT` (sichtbarer Link-Text muss exakt passen)
- `By.PARTIAL_LINK_TEXT`
- `By.CSS_SELECTOR`
- `By.XPATH` (mächtig, aber kann fragil sein)

---

## 4) Infos auslesen

```python
driver.title
driver.current_url

h1.text
h1.get_attribute("href")      # z.B. bei <a>
h1.get_attribute("class")
```

**Status / Sichtbarkeit**
```python
elem.is_displayed()
elem.is_enabled()
elem.is_selected()  # z.B. Checkbox/Radio
```

---

## 5) Checks / Assertions (Smoke Tests)

```python
assert "Reutlingen" in driver.title

h1 = driver.find_element(By.TAG_NAME, "h1")
assert ("Hochschule" in h1.text) or ("Reutlingen" in h1.text)

nav = driver.find_element(By.LINK_TEXT, "Studium")
assert nav.is_displayed()
```

---

## 6) Interaktionen (Click, Input, Clear)

```python
button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary")
button.click()

inp = driver.find_element(By.NAME, "username")
inp.clear()
inp.send_keys("demo")
```

---

## 7) Waits (Best Practice)

### Warum Waits?
Moderne Seiten laden Inhalte **asynchron** (AJAX, Lazy Loading, Animationen).  
`time.sleep()` ist **fragil**: zu kurz → flaky, zu lang → langsam.

### Standard-Pattern (Explicit Wait)
```python
elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
```

### Click-sicher warten
```python
btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary")))
btn.click()
```

---

## 8) Expected Conditions (EC) – häufige Beispiele

> Alle EC-Methoden arbeiten typischerweise mit **(By, locator)** Tuple.

### Präsenz / Sichtbarkeit / Klickbarkeit
```python
EC.presence_of_element_located((By.CSS_SELECTOR, "..."))     # existiert im DOM
EC.visibility_of_element_located((By.CSS_SELECTOR, "..."))   # sichtbar (display/size)
EC.element_to_be_clickable((By.CSS_SELECTOR, "..."))         # sichtbar + enabled
```

### Unsichtbar / Weg
```python
EC.invisibility_of_element_located((By.CSS_SELECTOR, "..."))
EC.staleness_of(element)  # Element ist "alt" (DOM refresh/neu gerendert)
```

### Text prüfen
```python
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "Schon eingeloggt")
EC.text_to_be_present_in_element_value((By.NAME, "q"), "abc")  # für input value
```

### Titel / URL
```python
EC.title_contains("Reutlingen")
EC.url_contains("/studium")
EC.url_to_be("https://example.com")
```

### Alerts / Frames / Windows
```python
EC.alert_is_present()

EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#id"))

EC.number_of_windows_to_be(2)
```

**Beispiel: warten bis H1-Text erscheint**
```python
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "Reutlingen"))
```

---

## 9) CSS Selector Cheatsheet

### Basics
- Tag `<a ...>` → `a`
- Klasse `<a class="btn">` → `a.btn`
- Mehrere Klassen → `a.btn.btn-primary`
- Tag + ID `<div id="main">` → `div#main` oder `#main`

### Hierarchie
- Ein `<a>` irgendwo in `.menu` → `.menu a`
- Direktes Kind → `.menu > a`
- Direkt nach `<h2>` → `h2 + p`
- Späterer Nachbar (gleiche Ebene) → `h2 ~ p`

### Attribute
- Exakt → `a[href="/abc/def/ghi"]`
- Enthält → `a[href*="def"]`
- Beginnt mit → `a[href^="ab"]`
- Endet mit → `a[href$="ab"]`

### Häufige Kombis
- Button-Link nach Text (wenn stabil) eher über Attribute/Klassen als Text:
  - `a.btn.btn-primary[href*="veranstaltungen"]`

---

## 10) XPath (nur wenn nötig, mini)

```python
driver.find_element(By.XPATH, "//h1")
driver.find_element(By.XPATH, "//a[contains(@href,'veranstaltungen')]")
driver.find_element(By.XPATH, "//*[normalize-space()='Login']")  # exakter Text (Whitespace-normalisiert)
```

---

## 11) Häufige Probleme (und schnelle Fixes)

### `NoSuchElementException`
- Element ist noch nicht da → **Explicit Wait** nutzen
- Falscher Locator (Text/Case/Whitespace) → im DOM prüfen

### `TimeoutException`
- Bedingung nie erfüllt → Locator prüfen, andere EC nutzen (z.B. `presence` statt `clickable`)

### Flakiness / Instabil
- Kein `sleep()`-Gambling → **wait.until(...)**
- Zu fragile Selektoren vermeiden (dynamische Klassen/IDs)

---

## 12) Mini-Template: „Stabiler Testablauf“

```python
driver.get("https://www.reutlingen-university.de/")

# Warten bis Seite "ready genug" ist (z.B. H1 sichtbar)
h1 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

assert "Reutlingen" in driver.title
assert h1.text.strip() != ""

# Navigation vorhanden?
nav = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Studium")))
assert nav.is_displayed()
```

---

