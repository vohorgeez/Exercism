def can_chain(dominoes):
    if dominoes == []:
        return []
    track = []
    remaining = dominoes.copy()

    count = {}
    for domino in dominoes:
        for i in range(2):
            if domino[i] not in count.keys():
                count[domino[i]] = 1
            else:
                count[domino[i]] += 1
    optimal_value = max(count, key=count.get)
    
    security_check = 0
    while remaining != [] and security_check != 1000:
        security_check += 1
        for domino in remaining:
            for i in range(2):
                if track == [] and domino[i] == optimal_value:
                    track.append(domino) if i == 0 else track.append((domino[1], domino[0]))
                    remaining.remove(domino)
                    break
                elif track == [] and domino[i] != optimal_value:
                    continue
                elif domino[i] == track[-1][1]:
                    track.append(domino) if i == 0 else track.append((domino[1], domino[0]))
                    remaining.remove(domino)
                    break
    
    if security_check == 1000:
        return None
    if track[0][0] == track[-1][1]:
        return track
    else:
        return None