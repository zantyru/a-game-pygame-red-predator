from dataclasses import dataclass

import pygame as pg


COLOR_DEFAULT = "black"
COLOR_PLAYER = "red"
COLOR_FOOD = "green"
COLOR_BACKGROUND = "#f0f8f0"

SCREEN_SIZE = pg.Vector2(800.0, 600.0)


@dataclass
class Entity:
    color: pg.Color = COLOR_DEFAULT
    speed: float = 0.0
    position: pg.Vector2 = pg.Vector2()
    dposition: pg.Vector2 = pg.Vector2()


def start():
    pass


if __name__ == "__main__":
    start()