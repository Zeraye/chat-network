import pygame_textinput
import pygame
import time
from network import Network

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


def write_to_conv(text, user, user2, conv):
    if len(text) != 7:
        user.conv_add(text)
        user2.conv_add(text)
    if len(conv) > 43:
        user.remove_word()
        user2.remove_word()


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
    conv = []
    n = Network()
    user = n.get_p()
    timer = time.time()
    user2 = n.send(user)
    delay = 1
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        length = len(user2.get_conv())
        user2 = n.send(user)
        print('USER CONV')
        print(user.get_conv())
        print('USER2 CONV')
        print(user2.get_conv())
        if len(user.get_conv()) != 0:
            conv.append(user.get_conv()[-1])
            user.set_conv([])
        if len(user2.get_conv()) != 0:
            conv.append(user2.get_conv()[-1])
            user2.set_conv([])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_BACKSPACE:
                    if not event.key == pygame.K_LSHIFT:
                        if not event.key == pygame.K_LCTRL:
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
                    write_to_conv(user.get_name() + ': ' + textinput.get_text(), user, user2, conv)
                    print(textinput.get_text())
                    textinput.clear_text()
                    timer = time.time()

        textinput.update(events)

        draw(win, user.get_words(), conv)

    pygame.quit()


if __name__ == '__main__':
    main(WIN)
