import pygame_textinput
import pygame
import time
from network import Network
from database import Database
from menu import main_menu
from menu import user

pygame.init()

WIDTH = 500
HEIGHT = 900

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chat')

font = pygame.font.SysFont('lucidaconsole', 20)
textinput = pygame_textinput.TextInput(font_size=20,
                                       font_family='lucidaconsole',
                                       text_color=(255, 255, 255),
                                       cursor_color=(255, 255, 255))


def draw_textinput(win):
    pygame.draw.rect(win, RED, (0, HEIGHT - 40, 500, 40))
    win.blit(textinput.get_surface(), (10, HEIGHT - 30))


def write_to_conv(text, user):
    if len(text) != len(user.get_name()) + 2:
        user.conv_add(text)


def draw_conv(win, conv):
    i = 0
    while i < len(conv):
        textsurface = font.render(conv[i], False, WHITE)
        win.blit(textsurface, (0, i * 20))
        i += 1


def draw_limit(win, words):
    textsurface = font.render(str(words) + '/' + '30', False, WHITE)
    win.blit(textsurface, (500 - textsurface.get_width() * 1.1, HEIGHT - 30))


def draw(win, words, conv):
    win.fill((0, 0, 0))
    draw_conv(win, conv)
    draw_textinput(win)
    draw_limit(win, words)
    pygame.display.update()


def main(win):
    main_menu(win)
    conv = Database().get()
    draw(win, user.get_words(), conv)
    timer = time.time()
    delay = 1
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        conv = Database().get()
        if len(Database().get()) > 43:
            Database().remove()
            conv = Database().get()
        if len(user.get_conv()) != 0:
            Database().add(user.get_conv()[-1])
            user.set_conv([])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_BACKSPACE:
                    if not event.key == pygame.K_LSHIFT:
                        if not event.key == pygame.K_LCTRL:
                            if not event.key == pygame.K_RETURN:
                                user.add_word()
                if event.key == pygame.K_BACKSPACE and user.get_words() > 0:
                    user.remove_word()
                if user.get_words() > 30:
                    textinput.input_string = (
                            textinput.input_string[:max(textinput.cursor_position - 1, 0)]
                            + textinput.input_string[textinput.cursor_position:]
                    )
                    textinput.cursor_position = max(textinput.cursor_position - 1, 0)
                    user.remove_word()

                if event.key == pygame.K_RETURN and time.time() - timer > delay:
                    user.reset_words()
                    write_to_conv(user.get_name() + ': ' + textinput.get_text(), user)
                    print(textinput.get_text())
                    textinput.clear_text()
                    timer = time.time()

        textinput.update(events)

        draw(win, user.get_words(), conv)

    pygame.quit()


if __name__ == '__main__':
    main(WIN)