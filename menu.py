import pygame_textinput
import pygame
from network import Network
from database import Database
from user import User
import json

WIDTH = 500
HEIGHT = 900

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('lucidaconsole', 40)
textinput = pygame_textinput.TextInput(font_size=30,
                                       font_family='lucidaconsole',
                                       text_color=(255, 255, 255),
                                       cursor_color=(255, 255, 255))

n = Network()
user = n.get_p()


def write_json(data, filename='users.json'):
    with open(filename, 'r+') as f:
        json.dump(data, f, indent=4)


def draw_textinput(win):
    textsurface = font.render('ENTER YOUR NAME', False, WHITE)
    pygame.draw.rect(win, RED, (WIDTH * 0.05, HEIGHT * 0.38, WIDTH * 0.9, 140))
    win.blit(textsurface, ((WIDTH - textsurface.get_width()) / 2, (HEIGHT - 4 * textsurface.get_height()) / 2))
    win.blit(textinput.get_surface(), ((WIDTH - textinput.get_surface().get_width()) / 2, (HEIGHT - textinput.get_surface().get_height()) / 2))


# def draw_limit(win, words):
#     textsurface = font.render(str(words) + '/' + '30', False, WHITE)
#     win.blit(textsurface, (500 - textsurface.get_width() * 1.1, HEIGHT - 30))


def draw(win):
    win.fill((0, 0, 0))
    draw_textinput(win)
    # draw_limit(win, words)
    pygame.display.update()


def main_menu(win):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = textinput.get_text()
                    with open('users.json', 'r+') as file:
                        new_data = {str(user.get_number()): [str(name), str(user.get_number()), 'USER', []]}
                        data = json.loads(file.read())
                        data.update(new_data)
                        write_json(data)
                        user.change_name(str(name))
                    textinput.clear_text()
                    run = False
                    break

            textinput.update(events)

        draw(win)
