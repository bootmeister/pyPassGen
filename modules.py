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

def leet(orig_word):
    try:
        orig_word = int(orig_word)
    except ValueError:
        import rules
        from random import randint
        word = []
        for char in orig_word:
            for rule in rules.rules:
                if char in rule:
                    word.append(rule[randint(0, len(rule) - 1)])
                    break
        return "".join(word)
    return str(orig_word)

    
def shuffle(word, methods):
    if methods["reverse"]: 
        word = word[::-1]
    if methods["leet"]: 
        word = leet(word)
    return word


def get_methods():
    methods = {"reverse": False, "leet": False}
    print("""    Secenegi iptal etmek icin 0 seciniz.
    Kabul etmek icin herhangi bir sayiyi secebilirsiniz.""")
    
    for method in methods:
        methods[method] = bool(int(input(method + ": ")))
    return methods
