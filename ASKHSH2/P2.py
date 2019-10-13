FILENAME = "P2text.txt"

f = open(FILENAME, "r")

spaces = 0
tabs = 0
non_printables = 0

for character in f.read():
    if character == " ":
        spaces +=1
    elif character == '\t':
        tabs += 1
    elif character.isprintable() == False:
        non_printables += 1

fcr = open("results.txt", "w+")

List = ["Spaces: " + spaces.__str__(), '\n'  "Tabs: " + tabs.__str__(), '\n' "Non-Printable Characters: " + non_printables.__str__()]

fcr.writelines(List)

f.close()
fcr.close()

print("The results' file is created in the folder.")
