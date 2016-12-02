from random import randint


def get_kwords():
    while True:
        try:
            count = int(input("Kac kelime gircen: "))
            break
        except ValueError:
            print("Olmadi sayi gir")
        
    kwords = []
    while count > 0:
        kwords.append(str(input("Gir: ")))
        count = count - 1
    return kwords

def leet(word):
    ajsdjajajsdkjakjsd You are here hashdahsdas

def shuffle(word, methods):
    if method["reverse"] == True:
        word = reverse(word)
    elif method["leet"] == True:
        word = leet(word)


def get_tf(sec):
    pass


def get_methods():
    methods = {"reverse": False, "leet": False}
    print("Secenegi iptal etmek icin 0 seciniz")
    
    for method in methods:
        methods[method] = bool(input(method))
