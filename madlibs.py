# ~~~~~ HELPER FUNCTIONS AND IMPORTS ~~~~~
def madLibs(noun1, noun2, noun3, noun4, noun5, adj1, adj2, adj3, adj4, verb1, verb2, verb3):
    print(f"""~~~~~ The Incident on Planet {noun1} ~~~~~\n
            Captain {noun2} adjusted the controls of the starship, feeling unusually {adj1} about their mission. The crew had been sent to investigate a mysterious signal coming from a {adj2} region of space near Planet {noun1}.\n
            As they landed, a strange {noun3} emerged from the shadows and began to {verb1} loudly. “This is highly {adj3},” whispered the ship’s AI, refusing to {verb2} any further analysis.\n
            Suddenly, the ground beneath them started to {verb3}, revealing a hidden chamber filled with glowing {noun4}s. At the center stood a {adj4} artifact shaped like a {noun5}.\n
            Captain {noun2} took one step closer… and immediately regretted it.""")



# ~~~~~ MAIN FUNCTION DEFINITION ~~~~~
def main():
    n1 = input("Enter a noun: ")
    n2 = input("Enter a second noun: ")
    n3 = input("Enter a third noun: ")
    n4 = input("Enter a fourth noun: ")
    n5 = input("Enter a fifth noun: ")

    a1 = input("Enter a adjective: ")
    a2 = input("Enter a second adjective: ")
    a3 = input("Enter a third adjective: ")
    a4 = input("Enter a fourth adjective: ")

    v1 = input("Enter a verb: ")
    v2 = input("Enter a second verb: ")
    v3 = input("Enter a third verb: ")

    madLibs(n1, n2, n3, n4, n5, a1, a2, a3, a4, v1, v2, v3)

# ~~~~~ MAIN FUNCTION CALL ~~~~~
main()
