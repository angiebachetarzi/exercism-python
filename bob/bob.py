def response(hey_bob):
    message = hey_bob.strip()
    if not message:
        return "Fine. Be that way!"
    if message.isupper():
        if message[-1] == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    if message[-1] == '?':
        return "Sure."
    return "Whatever."
