import pygame_textinput
import pygame


class User:
    def __init__(self, name, perms, conv, words=0):
        self.name = name
        self.perms = perms
        self.words = words
        self.conv = conv

    def get_name(self):
        return self.name

    def get_perms(self):
        return self.perms

    def add_word(self):
        self.words += 1

    def remove_word(self):
        self.words -= 1

    def get_words(self):
        return self.words

    def reset_words(self):
        self.words = 0

    def get_conv(self):
        return self.conv

    def conv_add(self, message):
        self.conv.append(message)

    def conv_remove(self):
        self.conv.pop(0)

    def set_conv(self, new_conv):
        self.conv = new_conv
