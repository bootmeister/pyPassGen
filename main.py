import modules

kwords = modules.get_kwords()
methods = modules.get_methods(methods)

passwd = []
for word in kwords:
    passwd.append(modules.shuffle(word, methods))

passwd = modules.shuffle(passwd, methods)

print(passwd)
