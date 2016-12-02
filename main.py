import modules

kwords = modules.get_kwords()
options = modules.get_options()

passwd = []
for word in kwords:
    passwd.append(modules.shuffle(word, options))



passwd = modules.shuffle(passwd)

print(passwd)