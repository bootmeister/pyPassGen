import modules

kwords = modules.get_kwords()
methods = modules.get_methods()

passwd = []
for word in kwords:
    passwd.append(modules.shuffle(word, methods))

print("".join(passwd))
