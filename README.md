# Selenium Workshop – Installationsanleitung

## 1. Aufgabe 0 – Vorbereitung

Diese Anleitung führt dich durch alle notwendigen Schritte, um das Workshop-Projekt lokal auszuführen.

> **Hinweis:** Du kannst jede IDE verwenden (VS Code, IntelliJ, PyCharm, …)

---

## 2. Voraussetzungen

- Laptop mit Windows / macOS / Linux
- Internet-Zugang
- Rechte, Software zu installieren
- **Google Chrome**
- **Git** (zum Klonen des Repos)

---

## 3. Python installieren (3.13)

### 3.1 Python-Version prüfen

1. Terminal / Eingabeaufforderung öffnen
2. Befehl eingeben:

```bash
python --version
```

oder (macOS/Linux manchmal üblich)

```bash
python3 --version
```

✅ Wenn eine Version wie `Python 3.13.x` angezeigt wird → passt.  
❌ Wenn der Befehl nicht gefunden wird oder die Version deutlich älter ist → installieren/aktualisieren.

### 3.2 Python installieren (falls nicht vorhanden)

1. Python 3.13 von der offiziellen Website herunterladen: https://www.python.org/downloads/
2. **Windows:** Beim Installer unbedingt **„Add Python to PATH“** anhaken.
3. Terminal schließen & neu öffnen
4. Version erneut prüfen:

```bash
python --version
```

---

## 4. Projekt klonen (Git)

1. Terminal öffnen
2. In ein Verzeichnis wechseln, in dem du arbeiten willst
3. Repository klonen:

```bash
git clone https://github.com/24Seconds03/Selenium_Workshop_Aufgaben.git
```

4. In den Projektordner wechseln:

```bash
cd Selenium_Workshop_Aufgaben
```

---

## 5. Virtuelle Umgebung erstellen (empfohlen)

### Windows (PowerShell / CMD)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Aktivierung prüfen:**  
Im Terminal sollte vorne `(.venv)` stehen.

Alternativ kann auch Conda verwendet werden.

---

## 6. Abhängigkeiten installieren (requirements.txt)

Sicherstellen, dass pip installiert ist:

```bash
pip --version
```

Falls pip nicht installiert ist, installieren mit:

```bash
python -m ensurepip --upgrade
```

Mit aktivierter virtueller Umgebung:

```bash
python -m pip install -r requirements.txt
```

Falls `python` nicht klappt (macOS/Linux):

```bash
python3 -m pip install -r requirements.txt
```

---

## 7. Installation testen

Wenn alles erfolgreich war, führe den Check aus:

```bash
python check_selenium_test.py
```

---

## 8. VS Code: Python Extensions installieren

In den VS Code Extensions -> Python
Folgende Extenisions installieren:

- Python Debugger
- Python
- Pylance
- Python Environments

Stelle sicher, dass die Nutzereinstellung "python.useEnvironmentsExtension": true gesetzt ist.

## 9. Häufige Probleme und Lösungen

| Problem | Lösung |
|---------|--------|
| `python: Befehl nicht gefunden` | Python ist nicht im PATH. Unter Windows: Neuinstallation mit **„Add Python to PATH“** |
| `ModuleNotFoundError: No module named 'selenium'` | Stelle sicher, dass `.venv` aktiv ist und `pip install -r requirements.txt` ausgeführt wurde |
| `Permission denied` (macOS/Linux) | venv aktivieren, ggf. `python3 -m pip ...` nutzen |
| `pip: Befehl nicht gefunden` | `python -m pip install ...` verwenden |
| Git fehlt | Git installieren: https://git-scm.com/downloads |

---

**Fragen?** Bei Problemen bitte Workshop-Leitung kontaktieren.
