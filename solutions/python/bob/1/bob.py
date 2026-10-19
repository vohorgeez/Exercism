def response(hey_bob):
    silence = (hey_bob == None) or (hey_bob.isspace()) or (hey_bob == "")
    if silence:
        return "Fine. Be that way!"
    question = ("".join(hey_bob.split())[-1] == '?')
    yelled = (hey_bob == hey_bob.upper()) and (any(c.isalpha() for c in hey_bob))
    if question and yelled:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif yelled:
        return "Whoa, chill out!"
    else:
        return "Whatever."