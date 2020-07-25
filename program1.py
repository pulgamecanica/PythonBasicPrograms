def joinMe(newLine):
    interroagatives = ("how", "what", "why")
    capitalized = newLine.capitalize()
    if newLine.lower().startswith(interroagatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(joinMe("How are you"))
print(joinMe("hello darling"))

arraySentences = []
while True:
    user_input = input ("Say something: ")
    if user_input == "\end":
        break
    else:
        arraySentences.append(joinMe(user_input))
        continue

print(" ".join(arraySentences))