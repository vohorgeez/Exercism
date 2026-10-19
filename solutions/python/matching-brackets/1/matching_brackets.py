def is_paired(input_string):
    open_brack = 0
    open_brace = 0
    open_par = 0
    pile = ["start"]
    for char in input_string:
        if char == "[":
            open_brack += 1
            pile.append("brack")
        if char == "{":
            open_brace += 1
            pile.append("brace")
        if char == "(":
            open_par += 1
            pile.append("par")
        if char == "]":
            if pile[-1] != "brack":
                return False
            pile.pop()
            open_brack -= 1
        if char == "}":
            if pile[-1] != "brace":
                return False
            pile.pop()
            open_brace -= 1
        if char == ")":
            if pile[-1] != "par":
                return False
            pile.pop()
            open_par -= 1
    return open_brack == 0 and open_brace == 0 and open_par == 0