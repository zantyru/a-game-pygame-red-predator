from dataclasses import dataclass, field

import pygame as pg


TARGET_FPS = 60
MILLISECONDS_PER_SECOND = 1000

COLOR_DEFAULT = "black"
COLOR_PLAYER = "red"
COLOR_FOOD = "green"
COLOR_BACKGROUND = "#f0f8f0"

SCREEN_SIZE = pg.Vector2(800.0, 600.0)


@dataclass
class Entity:
    color: pg.Color = COLOR_DEFAULT
    speed: float = 0.0
    position: pg.Vector2 = field(default_factory=pg.Vector2)
    dposition: pg.Vector2 = field(default_factory=pg.Vector2)


def start():
    
    pg.init()
    surface_screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()
    is_gameplay = True
    dt = 0.0
    
    entity_player = Entity(
        color=COLOR_PLAYER,
        speed=10.0,
        position=SCREEN_SIZE * 0.5,
    )
    
    entities = [
        entity_player,
    ]
    
    while is_gameplay:
        
        # - Отрисовка -
        surface_screen.fill(COLOR_BACKGROUND)
        ... # Тут будет отрисовка сущностей
        pg.display.flip()
        
        # - Опрос событий -
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_gameplay = False
        
        # - Игровая логика -
        dt = clock.tick(TARGET_FPS) / MILLISECONDS_PER_SECOND
    
    pg.quit()
    

if __name__ == "__main__":
    start()