from random import random as get_random_float
from dataclasses import dataclass, field

import pygame as pg


TARGET_FPS = 60
MILLISECONDS_PER_SECOND = 1000

COLOR_DEFAULT = "black"
COLOR_PLAYER = "red"
COLOR_FOOD = "green"
COLOR_BACKGROUND = "#f0f8f0"

SCREEN_SIZE = pg.Vector2(800.0, 600.0)

ENTITY_TYPE_STATIC = 0
ENTITY_TYPE_PLAYER = 1
ENTITY_TYPE_FOOD = 2


@dataclass
class Entity:
    type: int = ENTITY_TYPE_STATIC
    color: pg.Color = COLOR_DEFAULT
    speed: float = 0.0
    position: pg.Vector2 = field(default_factory=pg.Vector2)
    dposition: pg.Vector2 = field(default_factory=pg.Vector2)


def draw_entity_static(surface: pg.Surface, entity: Entity) -> None:
    pass


def draw_entity_player(surface: pg.Surface, player: Entity) -> None:
    
    pg.draw.circle(
        surface=surface,
        color=player.color,
        center=player.position,
        radius=20,  #@TODO Убрать магическое число
    )


def draw_entity_food(surface: pg.Surface, food: Entity) -> None:
    
    pg.draw.circle(
        surface=surface,
        color=food.color,
        center=food.position,
        radius=10,  #@TODO Убрать магическое число
    )


def update_entity_static(dt: float, player: Entity) -> None:
    pass


def update_entity_player(dt: float, player: Entity) -> None:
    
    keys = pg.key.get_pressed()
    
    player.dposition.x = 0.0
    player.dposition.y = 0.0
    
    if keys[pg.K_w]:
        player.dposition.y += -1.0
    
    if keys[pg.K_s]:
        player.dposition.y += 1.0
        
    if keys[pg.K_a]:
        player.dposition.x += -1.0
    
    if keys[pg.K_d]:
        player.dposition.x += 1.0
        
    if player.dposition.x or player.dposition.y:
        player.dposition.normalize_ip()
    
    player.position += player.speed * player.dposition * dt


def update_entity_food(dt: float, food: Entity) -> None:
    
    food.dposition.x = get_random_float() * 2.0 - 1.0
    food.dposition.y = get_random_float() * 2.0 - 1.0
        
    if food.dposition.x or food.dposition.y:
        food.dposition.normalize_ip()
    
    food.position += food.speed * food.dposition * dt


def start():
    
    pg.init()
    surface_screen = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()
    is_gameplay = True
    dt = 0.0
    
    entity_player = Entity(
        type=ENTITY_TYPE_PLAYER,
        color=COLOR_PLAYER,
        speed=100.0,
        position=SCREEN_SIZE * 0.5,
    )
    
    entities = [
        entity_player,
        Entity(
            type=ENTITY_TYPE_FOOD,
            color=COLOR_FOOD,
            speed=300.0,
            position=SCREEN_SIZE * get_random_float(),
        ),
        Entity(
            type=ENTITY_TYPE_FOOD,
            color=COLOR_FOOD,
            speed=300.0,
            position=SCREEN_SIZE * get_random_float(),
        ),
        Entity(
            type=ENTITY_TYPE_FOOD,
            color=COLOR_FOOD,
            speed=300.0,
            position=SCREEN_SIZE * get_random_float(),
        ),
    ]
    
    draw_functions_by_entity_type = {
        ENTITY_TYPE_STATIC: draw_entity_static,
        ENTITY_TYPE_PLAYER: draw_entity_player,
        ENTITY_TYPE_FOOD: draw_entity_food,
    }
    
    update_functions_by_entity_type = {
        ENTITY_TYPE_STATIC: update_entity_static,
        ENTITY_TYPE_PLAYER: update_entity_player,
        ENTITY_TYPE_FOOD: update_entity_food,
    }
    
    while is_gameplay:
        
        # - Отрисовка -
        surface_screen.fill(COLOR_BACKGROUND)
        
        for entity in entities:
            draw_functions_by_entity_type[entity.type](surface_screen, entity)
            
        pg.display.flip()
        
        # - Опрос событий -
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_gameplay = False
        
        # - Игровая логика -
        for entity in entities:
            update_functions_by_entity_type[entity.type](dt, entity)
        
        dt = clock.tick(TARGET_FPS) / MILLISECONDS_PER_SECOND
    
    pg.quit()
    

if __name__ == "__main__":
    start()