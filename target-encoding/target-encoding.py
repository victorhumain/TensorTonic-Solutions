def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    n = len(categories)
    output = [0]*n
    dictionnaire = {}
    for i in range(n):
        if categories[i] in dictionnaire.keys():
            dictionnaire[categories[i]].append(targets[i])
        else:
            dictionnaire[categories[i]] = [targets[i]]
    for i in range(n):
        item = categories[i]
        output[i] = sum(dictionnaire[item])/len(dictionnaire[item])
    return output