def test_combinations(n, list, combi=[]):
    
    if combi is None:
        combi = []

    if len(list) == n:
        if combi.count(list) == 0:
            combi.append(list)
            combi.sort()
        return combi
    else:
        for i in range(len(list)):
            result_list = list[:i] + list[i+1:]
            combi = test_combinations(n, result_list, combi)
        return combi


print test_combinations(2,[1,2,3,4])



