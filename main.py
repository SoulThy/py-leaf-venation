import pygame
import time
import random

BACKGROUND_COLOR = "gray10"
WIDTH_SIZE, HEIGHT_SIZE = 1280, 1280
#STARTING_POS = pygame.Vector2(WIDTH_SIZE / 2, HEIGHT_SIZE / 2)
STARTING_POS = pygame.Vector2(0,0)

NODE_COLOR, SEED_COLOR = "green4", "gray"
NODE_RADIUS = 5 

AUXIN_COLOR = "red2"
AUXINS_DENSITY = 4
AUXIN_RADIUS = 5 
AUXIN_COLLISION_RADIUS = 5 * AUXIN_RADIUS 

AUTO_MODE = True
FPS = 30 
MAX_NODES = 20000

nodes = []
auxins = []

class Node:
    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.dir_to_auxins = []

    def draw(self, screen):
        pygame.draw.circle(screen, NODE_COLOR, self.pos, NODE_RADIUS)
        pygame.draw.circle(screen, SEED_COLOR, self.pos, NODE_RADIUS / 2)

class Auxin:
    def __init__(self, pos: pygame.Vector2):
        self.pos = pos
        self.closest_node = None

    def draw(self, screen):
        pygame.draw.circle(screen, AUXIN_COLOR, self.pos, AUXIN_RADIUS)

    def draw_collision_radius(self, screen):
        pygame.draw.circle(screen, AUXIN_COLOR, self.pos, AUXIN_COLLISION_RADIUS, 1)

    def draw_line_to_closest(self, screen):
        pygame.draw.aaline(screen, "gray25", self.pos, self.closest_node.pos, 1)

def update_closest_nodes():
    for auxin in auxins:
        closest_node = nodes[0]
        dist_to_closest = auxin.pos.distance_squared_to(closest_node.pos)

        for node in nodes:
            d = auxin.pos.distance_squared_to(node.pos) 
            if d < dist_to_closest:
                closest_node = node
                dist_to_closest = d

        auxin.closest_node = closest_node 

def spawn_auxins():
    collision_radius_sq = AUXIN_COLLISION_RADIUS ** 2

    for _ in range(AUXINS_DENSITY):
        is_collision = False
        x = random.randint(0, WIDTH_SIZE)
        y = random.randint(0, HEIGHT_SIZE)
        new_pos = pygame.Vector2(x,y) 

        for auxin in auxins:
            if new_pos.distance_squared_to(auxin.pos) < collision_radius_sq:
                is_collision = True
                break

        if not is_collision:
            for node in nodes:
                if new_pos.distance_squared_to(node.pos) < collision_radius_sq:
                    is_collision = True
                    break

        if not is_collision:
            new_auxin = Auxin(new_pos)
            auxins.append(new_auxin)

def populate_dir_to_auxins():
    for auxin in auxins:
        v = (auxin.pos - auxin.closest_node.pos).normalize()
        auxin.closest_node.dir_to_auxins.append(v)

def expand_nodes():
    for node in nodes[:]:
        if node.dir_to_auxins:
            s = sum(node.dir_to_auxins, pygame.Vector2(0,0)).normalize()
            new_node = Node(node.pos + (s * 2 * NODE_RADIUS))
            nodes.append(new_node)

        node.dir_to_auxins.clear() 

def check_auxin_collisions():
    global auxins
    collision_radius_sq = AUXIN_COLLISION_RADIUS ** 2
    surviving_auxins = []
    
    for auxin in auxins:
        is_collision = False
        for node in nodes:
            if auxin.pos.distance_squared_to(node.pos) < collision_radius_sq:
                is_collision = True
                break

        if not is_collision:
            surviving_auxins.append(auxin)

    auxins = surviving_auxins

def draw(screen):
    screen.fill(BACKGROUND_COLOR)

    for auxin in auxins:
        auxin.draw_line_to_closest(screen)
        auxin.draw(screen)
        auxin.draw_collision_radius(screen)

    for node in nodes:
        node.draw(screen)

    pygame.display.flip()

def step_simulation():
    populate_dir_to_auxins()
    expand_nodes()
    check_auxin_collisions()
    spawn_auxins() 
    update_closest_nodes()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_SIZE, HEIGHT_SIZE))
    clock = pygame.time.Clock()

    nodes.append(Node(STARTING_POS))

    while not auxins:
        spawn_auxins()
    update_closest_nodes()

    draw(screen)

    running = True
    simulation_started = False

    while running:
        if AUTO_MODE and len(nodes) < MAX_NODES and simulation_started:
            step_simulation()
            draw(screen)
            clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    break
        
                if event.key == pygame.K_SPACE and not AUTO_MODE:
                    step_simulation()
                    draw(screen)

                if event.key == pygame.K_s:
                    simulation_started = True

    pygame.quit()

if __name__ == "__main__":
    main()
