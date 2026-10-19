def tally(rows):
    table = {}
    for row in rows:
        data = row.split(';')
        for i in range(2):
            if data[i] not in table:
                table[data[i]] = {
                    "matches_played":0,
                    "matches_won":0,
                    "matches_drawn":0,
                    "matches_lost":0,
                    "points":0
                }
        table[data[0]]["matches_played"] += 1
        table[data[1]]["matches_played"] += 1
        if data[2] == "win":
            table[data[0]]["matches_won"] += 1
            table[data[1]]["matches_lost"] += 1
            table[data[0]]["points"] += 3
        elif data[2] == "draw":
            table[data[0]]["matches_drawn"] += 1
            table[data[1]]["matches_drawn"] += 1
            table[data[0]]["points"] += 1
            table[data[1]]["points"] += 1
        elif data[2] == "loss":
            table[data[1]]["matches_won"] += 1
            table[data[0]]["matches_lost"] += 1
            table[data[1]]["points"] += 3
    table = dict(sorted(table.items()))
    table = dict(sorted(table.items(), key= lambda item: item[1]["points"], reverse=True))
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team in table.keys():
        output.append(team 
                      + " " * (31-len(team)) 
                      + "|" 
                      + " " * (3 - len(str(table[team]["matches_played"]))) 
                      + str(table[team]["matches_played"])
                      + " |"
                      + " " * (3 - len(str(table[team]["matches_won"]))) 
                      + str(table[team]["matches_won"])
                      + " |"
                      + " " * (3 - len(str(table[team]["matches_drawn"]))) 
                      + str(table[team]["matches_drawn"])
                      + " |"
                      + " " * (3 - len(str(table[team]["matches_lost"]))) 
                      + str(table[team]["matches_lost"])
                      + " |"
                      + " " * (3 - len(str(table[team]["points"]))) 
                      + str(table[team]["points"])
                      )
    return output