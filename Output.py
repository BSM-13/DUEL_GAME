#Output has it's own file so it can be imported into every file that needs printing
printChoice=1
file = None

def output(text):
    if printChoice == 1:
        print(text)
    if printChoice == 2:
        file.write(text + "\n")
