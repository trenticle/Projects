#create a function, sentence capitalization
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
         return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#print(sentence_maker('how are you'))
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(user_input)

print(" ".join(results))
#lesson points
# 1 define a function
# 2 then iterate (make a loop)
# 3 store the output (results.append), and concatenate the output(.join)



