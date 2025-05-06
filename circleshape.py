import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def isColliding(self, circle):
        # check for collision between self and circle
        # if distance between center of self and center of circle is 
        # less than or equal to the sum of the radii, return True
        return (pygame.math.Vector2.distance_to(self.position, circle.position) <= (self.radius+circle.radius))
