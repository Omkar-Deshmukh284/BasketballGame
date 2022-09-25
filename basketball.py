import pygame
import random
import sys
# sys.path("C:\\Users\\pravi\\anaconda3\\Lib\\site-packages")
from PIL import Image


pygame.init()

WIDTH = 800
HEIGHT = 600

YELLOW = (255, 255, 0)
BG = (0, 0, 0)

net_size = 100
net_pos = [WIDTH / 2, HEIGHT - 2 * net_size]

# net=pygame.image.load('basketball_net1.png')
basketball = pygame.image.load('basketball-new.png')
# net = pygame.image.load('basketball_net1.png')
# net = Image.open('basketball_net-new.png')
# net = net.resize((net_size, net_size))
net = pygame.image.load('net1.png')

SPEED = 10

ball_size = 64
ball_pos = [random.randint(0, WIDTH - ball_size), 0]
ball_list = [ball_pos]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("allura", 35)

score = 0


def draw_basketball_net(x, y):
    screen.blit(net, (x, y))


def draw_basketball(x, y):
    screen.blit(basketball, (x, y))


def set_level(game_score, speed):
    if game_score < 20:
        speed = 5
    elif game_score < 40:
        speed = 8
    elif game_score < 60:
        speed = 12
    elif game_score < 80:
        speed = 15
    elif game_score < 100:
        speed = 20
    elif game_score < 200:
        speed = 50
    else:
        speed = 80
    return speed


def drop_enemies(ball_list):
    delay = random.random()
    if len(ball_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - ball_size)
        y_pos = 0
        ball_list.append([x_pos, y_pos])


def draw_enemies(ball_list):
    for ball_pos in ball_list:
        # pygame.draw.rect(screen, RED, (ball_pos[0], ball_pos[1], ball_size, ball_size))
        draw_basketball(ball_pos[0], ball_pos[1])


def update_ball_positions(ball_list):
    for idx, ball_pos in enumerate(ball_list):
        if ball_pos[1] >= 0 and ball_pos[1] < HEIGHT:
            ball_pos[1] += SPEED
        else:
            ball_list.pop(idx)


def collision_check(ball_list, net_pos):
    for ball_pos in ball_list:
        if detect_collision(ball_pos, net_pos):
            return True
    return False

def detect_collision(net_pos, ball_pos):
    p_x = net_pos[0]
    p_y = net_pos[1]

    e_x = ball_pos[0]
    e_y = ball_pos[1]

    if (e_x >= p_x and e_x < (p_x + net_size)) or (p_x >= e_x and p_x < (e_x + ball_size)):
        if (e_y >= p_y and e_y < (p_y + net_size)) or (p_y >= e_y and p_y < (e_y + ball_size)):
            return True


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = net_pos[0]
            y = net_pos[1]

            if event.key == pygame.K_LEFT:
                if x >= net_size:
                    x -= net_size
                else:
                    x = 0
            elif event.key == pygame.K_RIGHT:
                if x <= WIDTH:
                    x += net_size
                else:
                    x = WIDTH - net_size - 2

            net_pos = [x, y]

    screen.fill(BG)

    drop_enemies(ball_list)
    print('before collision check: ')
    print(score)
    if collision_check(ball_list, net_pos):
        score += 1
    print('after collision check: ')
    print(score)
    update_ball_positions(ball_list)
    # SPEED = set_level(score, SPEED)

    # print(score)
    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    # if detect_collision(net_pos, ball_pos):
    #     game_over = True

    # score = collision_check(ball_list, net_pos, score)
        # game_over = False

    game_over = False
    draw_enemies(ball_list)

    # pygame.draw.rect(screen, RED, (ball_pos[0], ball_pos[1], ball_size, ball_size))
    draw_basketball_net(net_pos[0], net_pos[1])

    clock.tick(30)

    pygame.display.update()
