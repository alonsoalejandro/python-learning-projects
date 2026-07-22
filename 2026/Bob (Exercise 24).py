def response(hey_bob):
    # Assuming hey_bob is str
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    has_letters = False

    for i in hey_bob:
        if i.isalpha():
            has_letters = True
            break

    question = hey_bob.endswith("?")
    yell = hey_bob.upper() == hey_bob and has_letters

    if yell and question:
        return "Calm down, I know what I'm doing!"
    elif yell and not question:
        return "Whoa, chill out!"
    elif question and not yell:
        return "Sure."
    else:
        return "Whatever."