def answer(question):
    if question[0:8] != "What is " or question[-1] != "?":
        raise ValueError("syntax error")
    question = question[7:-1]
    tokens = []
    operations = ['plus', 'multiplied', 'minus', 'divided']
    for word in question.split():
        if word.isdigit():
            tokens.append(int(word))
        elif word[0] == "-":
            if word[1:].isdigit():
                tokens.append(int(word))
        elif word in operations:
            tokens.append(word)
        elif word == 'by' and (tokens[-1] == 'multiplied' or tokens[-1] == 'divided'):
            continue
        elif word == 'What' or word == 'is':
            continue
        else:
            raise ValueError("unknown operation")
    for i in range(len(tokens)):
        if i % 2 == 0:
            if type(tokens[i]) is not int:
                raise ValueError("syntax error")
            if i == 0:
                result = tokens[i]
            else:
                if tokens[i-1] == 'plus':
                    result += tokens[i]
                if tokens[i-1] == 'multiplied':
                    result *= tokens[i]
                if tokens[i-1] == 'minus':
                    result -= tokens[i]
                if tokens[i-1] == 'divided':
                    result //= tokens[i]
        else:
            if type(tokens[i]) is not str or i == len(tokens) - 1:
                raise ValueError("syntax error")
    return result
                