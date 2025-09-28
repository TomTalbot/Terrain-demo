import pygame
import random
import os

class TerrainGenerator:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.TILE_SIZE = 32
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Terrain Generation Demo")
        
        # load and scale sprites
        self.dirt_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join('sprites', 'dirt_block.jpg')),
            (self.TILE_SIZE, self.TILE_SIZE)
        )
        self.grass_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join('sprites', 'grass_block.png')),
            (self.TILE_SIZE, self.TILE_SIZE)
        )
        
        self.SKY_COLOR = (135, 206, 235)
        self.terrain_blocks = []
        self.generate_terrain()

    def generate_terrain(self):
        self.terrain_blocks.clear()
        
        num_points = self.WIDTH // self.TILE_SIZE + 1
        current_height = self.HEIGHT // 2
        
        # generate terrain heights
        for x in range(0, self.WIDTH, self.TILE_SIZE):
            # height changes by -1, 0, or 1 blocks
            height_change = random.randint(-1, 1) * self.TILE_SIZE
            current_height += height_change
            current_height = max(self.HEIGHT//3, min(current_height, self.HEIGHT - self.TILE_SIZE * 3))
            
            # create blocks from height to bottom
            for y in range(current_height, self.HEIGHT, self.TILE_SIZE):
                block_type = 1 if y == current_height else 0  # 1 for grass, 0 for dirt
                self.terrain_blocks.append({
                    'rect': pygame.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE),
                    'type': block_type
                })

    def draw(self):
        self.screen.fill(self.SKY_COLOR)
        for block in self.terrain_blocks:
            sprite = self.grass_sprite if block['type'] == 1 else self.dirt_sprite
            self.screen.blit(sprite, block['rect'])
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.generate_terrain()
            
            self.draw()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = TerrainGenerator()
    game.run()