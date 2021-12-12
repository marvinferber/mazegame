# Maze Game (Labyrinth)
Das ist ein einfaches Labyrinth-Spiel zum Mitmachen. Spielfeld und Bot sollen selbst programmiert werden.

## Installation
Das Spiel benötigt Python als Laufzeitumgebung und einen Editor zum Programmieren des Bot.

Python kann hier heruntergeladen werden: https://www.python.org/downloads/

Als Editor empfehle ich Visual Studio Code: https://code.visualstudio.com/
Visual Studio Code besitzt folgende Erweiterungen, die für die Programmierung in Python sinnvoll sind.
- Pylance
- Python
Visual Studio Code hat noch weitere diverse Abhängigkeiten, die jedoch als Hinweisnachrichten aufploppen, die man dann nur bestätigen muss. Auch die Installation der deutschen Sprachpakete wird so automatisch vorgeschlagen.  

### Benötigte Python Bibliotheken
Zum Ausführen des Spiels wird die Python-Bibliothek windows-curses benötigt. Diese muss manuell installiert werden. Dazu öffnet ihr eine Pythonconsole und tippt Folgendes ein: `pip install windows-curses`

### Den Code laden
Zunächst braucht ihr natürlich noch den Quellcode zum Ausführen des Spiels. 

## Spiel starten
Wenn alles richtig installiert ist, könnt ihr das Spiel durch Doppelklick auf die Datei game.py starten. Ist kein Bot aktiv, dann kann man das Subjekt (¤) mit den Pfeiltasten zum Ausgang führen. Das Spiel läuft in einem Konsolenfenster. 
![](https://github.com/marvinferber/mazegame/wiki/content/console.png)

## Spielfelder
Ein Spielfeld besteht aus Wänden (#) und freien Strecken ( ). Der Rand des Spielfelds muss dabei zwingend durch Wände spezifiziert sein. Hier ein Beispiel:
```
##############
A #   #   # ##
# # #   # # ##
#   #####   ##
### ##### ####
# #   #   # ##
# # #   # # ##
#   ##### S ##
##############
```
Die besonderen Zeichen (S) für Startpunkt und (A) für Ausgang müssen jeweils einmalig im Spielfeld gesetzt werden. 

## Bot programmieren
Es ist möglich einen Bot zu programmieren, der aus Sicht des Subjekts versucht, im Labyrinth den Ausgang zu finden. 