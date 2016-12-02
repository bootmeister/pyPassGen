from random import randint
methods = {"reverse": False, "leet": False}


def get_kwords():
    count = int(input("Kac kelime gircen?"))
    kwords = []
    while count > 0:
        kwords.append(str(input("Gir: ")))
        count = count - 1
    return kwords


def shuffle(word, options=[True, True]):

    choice = len(options) - 1
    for method in methods:
        methods[method] = options[choice]



def get_tf(sec):
    pass


def get_options():
    print("Secenegi iptal etmek icin 0 seciniz")
    options = []
    for method in methods:
        options.append(bool(input(method)))

