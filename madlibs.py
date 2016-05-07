#! python3

message = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

adj = message.count("ADJECTIVE")
noun = message.count("NOUN")
verb = message.count("VERB")

# Adjectives
for i in range(1, adj + 1):
    prompt = "[{0}/{1}] Enter an adjective: ".format(
        i,
        adj
    )
    print(prompt, end="")
    user = input("")
    message = message.replace("ADJECTIVE", user, 1)

# Nouns
for i in range(1, noun + 1):
    prompt = "[{0}/{1}] Enter a noun: ".format(
        i,
        noun
    )
    print(prompt, end="")
    user = input("")
    message = message.replace("NOUN", user, 1)

# Verbs
for i in range(1, verb + 1):
    prompt = "[{0}/{1}] Enter a verb: ".format(
        i,
        verb
    )
    print(prompt, end="")
    user = input("")
    message = message.replace("VERB", user, 1)

print(message)

