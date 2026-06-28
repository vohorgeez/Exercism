def sum_of_multiples(limit, multiples):
    energy_points = set()
    for item in multiples:
        if item == 0:
            continue
        ep_for_this_item = set()
        if item <= limit:
            i=1
            while i*item < limit:
                ep_for_this_item.add(i*item)
                i+=1
            if not energy_points:
                energy_points = ep_for_this_item
            else:
                energy_points = energy_points.union(ep_for_this_item)
    total_energy_points = sum(energy_points)
    return total_energy_points