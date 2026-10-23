# PhotoRenamer

Kleine Windows-Desktop-App (Python/Tkinter), die Fotos und Videos anhand ihres Aufnahmedatums einheitlich umbenennt.

**Beispiel:** `34895782357.png` → `2018-01-01_00;00;00.png`

## Warum?

Kamera-, Handy- und Messenger-Dateien haben chaotische Namen. Mit einheitlichen Zeitstempeln sortiert sich ein Ordner automatisch chronologisch, auch wenn die Dateien von mehreren Geräten stammen.

## Features

- **Schneller Modus:** benennt alle Dateien eines Ordners automatisch um
- **Langsamer Modus:** öffnet jede Datei im Standard-Viewer, der vorgeschlagene Name lässt sich vor dem Umbenennen anpassen (inkl. Überspringen, Rückgängig und vorzeitigem Abbruch)
- **Datumsquellen** (in dieser Reihenfolge): EXIF → Erstellungsdatum → Datum im Dateinamen → Originalname
- Dark- und Light-Theme
- Log-Fenster mit Protokoll aller Aktionen

## Eindeutige Dateinamen

Gerätespezifische Namen wie `IMG_0001.jpg` kollidieren schnell, sobald Dateien von Handy, Kamera und Messenger in einem Ordner landen. PhotoRenamer benennt stattdessen nach dem **Zeitpunkt der Aufnahme** (auf die Sekunde genau). Jedes Foto bekommt damit einen Namen, der aus seinem Inhalt stammt und nicht vom Gerät, und die Dateien aller Geräte lassen sich ohne Überschneidungen zusammenführen.

Fällt trotzdem einmal dieselbe Sekunde zusammen (z. B. bei Serienaufnahmen), wird automatisch ein Zähler angehängt, z. B. `2018-01-01_00;00;00_1.jpg`. Es wird also nie eine Datei überschrieben.

Das Semikolon im Zeitstempel ersetzt den Doppelpunkt, der in Windows-Dateinamen nicht erlaubt ist.

## Tastenkürzel (Langsamer Modus)

| Taste       | Aktion                        |
| ----------- | ----------------------------- |
| `Enter`     | Umbenennen                    |
| `Esc`       | Überspringen                  |
| `Backspace` | Letzte Umbenennung rückgängig |

## Installation

Voraussetzung: Windows, Python 3.12+

```bash
pip install -r requirements.txt
python photo_renamer.py
```

## Als .exe bauen

```bash
pyinstaller PhotoRenamer.spec
```

Die fertige Datei liegt danach in `dist/`.

## Hinweise

- Es werden alle Dateien im gewählten Ordner umbenannt (ohne Unterordner), nicht nur Bilder.
- Der Langsame Modus schließt Viewer-Fenster (z. B. Fotos, VLC, Paint) nach dem Umbenennen automatisch.

## Technik

Python · Tkinter · Pillow (EXIF) · psutil · pywin32

## Autor

Matthrose
