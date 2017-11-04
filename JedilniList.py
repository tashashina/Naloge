print "Dnevni menu"

menu = {}
dat = open("menu.txt","w+")

while True:
    nova_jed = raw_input("Vnesi izbrano jed: ")
    menu[nova_jed] = raw_input("Vnesi ceno jedi: ")

    new = raw_input("Se zelis dodati jed? (da/ne)")

    if new.lower() == "ne":
        break

print menu

for item in menu:
    dat.write("%s, %s EUR \n" % (item, menu[item]))
    dat.write('\n ')

print "END"
dat.close()