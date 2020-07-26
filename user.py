class User:
    def __init__(self, name, number, perms='USER', conv=None, words=0):
        if conv is None:
            conv = []
        self.name = name
        self.number = number
        self.perms = perms
        self.words = words
        self.conv = conv

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def get_number(self):
        return self.number

    def get_perms(self):
        return self.perms

    def change_perms(self, new_perms):
        self.name = new_perms

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
