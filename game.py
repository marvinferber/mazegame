# -*- coding: utf-8 -*-
import time
import curses
from sys import exit
import threading


SÜD = 2
NORD = 0
OST = 1
WEST = 3

KEY_RIGHT = 454
KEY_LEFT = 452
KEY_DOWN = 456
KEY_UP = 450

def error(msg):
    print(msg)
    exit(-1)

def gamefieldToArray(thisfield):
    splitlines = thisfield.splitlines()
    arrfield = []
    start = (-1, -1)
    out = (-1, -1)
    x = 0
    for line in splitlines:
        arr = []
        y = 0
        for char in line:
            arr.append(char)
            if char == "S":
                start = (x, y)
            if char == "A":
                out = (x, y)
            y = y + 1
        x = x + 1
        arrfield.append(arr)
    return arrfield, start, out


class Bot:
    def __init__(self):
        self.blick = SÜD

    # Hier kommt die Logik für den Bot rein!
    # Der Bot kann nur nach NORD, SÜD, OST, WEST schauen
    # und dorthin gehen. Die Methode bewegen wird automatisch 
    # alle 0,5s aufgerufen. Somit kann der Bot alle 0,5s eine
    # Bewegung machen. Der Bot bekommt seine Umgebung durch ein 
    # Objekt "grenzen" gezeigt. Darin steht bspw. unter 
    # grenzen.SÜD ob sich dort eine Wand befindet (#) oder nicht ( ).
    # Zum Abschluss der Methode muss der Bot sagen was er machen möchte.
    # Dazu wird return aufgerufen und NORD, SÜD, WEST, OST oder -1
    # angegeben. Bei -1 bewegt sich der Bot in dieser Runde nicht. 
    # Läuft der Bot gegen eine Wand, passiert auch nichts!
    # Seine momentane Blickrichtung ist in self.blick gespeichert.
    # Auch diese kann NORD, SÜD, WEST, OST sein.
    def bewegen(self, grenzen):
        if grenzen[NORD] != "#":
            self.blick = NORD
            return self.blick
        if grenzen[OST] != "#":
            self.blick = OST
            return self.blick
        if grenzen[SÜD] != "#":
            self.blick = SÜD
            return self.blick
        if grenzen[WEST] != "#":
            self.blick = WEST
            return self.blick


class Gameplay:
    def __init__(self):
        self.running = True
        self.win = False
        with open('gamefield.txt') as f:
            self.gamefield = f.read()
        (self.arr, self.start, self.out) = gamefieldToArray(self.gamefield)
        if self.start[0] == -1:
            error("Kein Startpunkt spezifiziert!")
        else:
            self.x = self.start[0]
            self.y = self.start[1]
        if self.out[0] == -1:
            error("Kein Ausgang spezifiziert!")
        else:
            self.xout = self.out[0]
            self.yout = self.out[1]
        self.screen = curses.initscr()
        #self.screen.nodelay(1)
        curses.curs_set(0)
        self.screen.keypad(1)


    def keyboardloop(self):
        while self.running:
            key = self.screen.getch()
            if key == 113: # q
                self.running = False
                break  # q
            # handle arrow keys --> move
            self.arr[self.x][self.y] = " "
            if key == KEY_RIGHT:
                self.y = self.y + 1 if self.arr[self.x][self.y + 1] != "#" else self.y
            if key == KEY_LEFT:
                self.y = self.y - 1 if self.arr[self.x][self.y - 1] != "#" else self.y
            if key == KEY_UP:
                self.x = self.x - 1 if self.arr[self.x - 1][self.y] != "#" else self.x
            if key == KEY_DOWN:
                self.x = self.x + 1 if self.arr[self.x + 1][self.y] != "#" else self.x
            # check for win
            if (self.x == self.xout) and (self.y == self.yout):
                self.running = False
                self.win = True
            

    def botloop(self):
        bot = Bot()
        while self.running:
            # check for win
            if (self.x == self.xout) and (self.y == self.yout):
                self.running = False
                self.win=True
                break
            # prepare view for bot and call bot
            grenzen = {
                # keine Randbehandlung, da Spielfeld einen Rand hat
                SÜD: self.arr[self.x+1][self.y],
                NORD: self.arr[self.x-1][self.y],
                OST: self.arr[self.x][self.y+1],
                WEST: self.arr[self.x][self.y-1]
            }
            move = bot.bewegen(grenzen)
            self.arr[self.x][self.y] = " "
            if move == SÜD:
                self.x = self.x + 1 if self.arr[self.x + 1][self.y] != "#" else self.x
            if move == NORD:
                self.x = self.x - 1 if self.arr[self.x - 1][self.y] != "#" else self.x
            if move == OST:
                self.y = self.y + 1 if self.arr[self.x][self.y + 1] != "#" else self.y
            if move == WEST:
                self.y = self.y - 1 if self.arr[self.x][self.y - 1] != "#" else self.y
            time.sleep(.5)


if __name__ == '__main__':
    game = Gameplay()
    # keyboard listener
    threading.Thread(target=game.keyboardloop).start()
    # handle a bot
    #threading.Thread(target=game.botloop).start()
    # main gui loop
    while game.running:
        game.screen.clear()
        i = 0
        for line in game.arr:
            j = 0
            for char in line:
                if char == "#":
                    game.screen.addstr(i, j, u"\u2588".encode("utf-8"))
                else:
                    game.screen.addstr(i, j, char.encode("utf-8"))
                j = j + 1
            i = i + 1
        game.screen.addstr(game.x, game.y, u"\u00A4".encode("utf-8"))
        # add hints on Bottom
        game.screen.addstr(i, 0, u"Beenden: Taste <q> drücken!".encode("utf-8"))
        game.screen.refresh()
        time.sleep(0.05)
    if game.win:
        game.screen.addstr(0, 1, "Gewonnen!".encode("utf-8"))
    else:
        game.screen.addstr(0, 1, "Abbruch!".encode("utf-8"))
    game.screen.getch()
    curses.endwin()
    exit(0)
