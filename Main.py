import random
import pygame
import sys

def gen_meteor(meteor_pic):
    return {
        "mask": pygame.mask.from_surface(meteor_pic),
        "x": random.choice(range(10, 540, 50)),
        "y": random.choice(range(-10, -500, -50))
    }

def colision(mask1, mask2, mask1_coords, mask2_coords):
    x_off = mask2_coords[0] - mask1_coords[0]
    y_off = mask2_coords[1] - mask1_coords[1]
    if mask1.overlap(mask2, (x_off, y_off)):
        return True
    else: 
        return False

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    bg = pygame.image.load("background-3901037_1280.jpg")
    meteor_pic = pygame.image.load ("Meteor1.png")
    ss = pygame.image.load("spaceship.png")
    game_font = pygame.font.SysFont("bauhaus 93" ,30)
    window = pygame.display.set_mode((600,800))
    s_mask = pygame.mask.from_surface(ss)

    score = 0

    coordinates_x= 250
    coordinates_y= 720

    meteors = []
    meteor_speed=0
    meteor_increment=4
    meteor_count=0

    end = False

    while True:
        score_t = game_font.render(f"SCORE {score}", True, (255,255,255))

        if len(meteors) == 0: 
            meteor_speed += 1
            meteor_count += meteor_increment
            for i in range(meteor_count):
                meteors.append(gen_meteor(meteor_pic))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            if coordinates_x > 5:
                coordinates_x -= 3
        if keys[pygame.K_RIGHT]:
            if coordinates_x < 520:
                coordinates_x += 3
        if keys[pygame.K_UP]:
            if coordinates_y > 5:
                coordinates_y -= 3
        if keys[pygame.K_DOWN]:
            if coordinates_y < 720:
                coordinates_y += 3

        window.blit(bg, (0, 0))
        window.blit(ss,(coordinates_x, coordinates_y))

        if not end:
            for meteor in meteors[:]:
                window.blit(meteor_pic, (meteor['x'], meteor['y']))
                meteor["y"] += meteor_speed
                if meteor["y"] > 800:
                    score += 1
                    meteors.remove(meteor)
                if colision(s_mask, meteor['mask'], (coordinates_x, coordinates_y), (meteor['x'], meteor['y'])):
                    end=True
        
        if end:
            end_text = game_font.render("GAME OVER", True, (255, 255, 255))
            window.blit(end_text, (200, 400))

        window.blit(score_t, (10,10))
        pygame.display.update()
        clock.tick(60)
