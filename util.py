def tier(series):
    for j, value in enumerate(series):
        if value == value:
            return j + 1, value
    return None


def acess(area_dict, indice_names):
    temporary_dict = area_dict
    for tierName in indice_names:
        temporary_dict = temporary_dict[tierName]
    return temporary_dict


def acess2(area_dict, indice_names):
    temporary_dict = area_dict
    for tierName in indice_names[:-1]:
        temporary_dict = temporary_dict[tierName]
    return temporary_dict, indice_names[-1]


total = []


def get_leafs(dic, indice_names):
    dig(dic, indice_names)
    return total


def dig(dic, indice_names):
    global total
    novo_indice = indice_names.copy()
    if isinstance(dic, dict):
        for key in dic.keys():
            dig(dic[key], novo_indice + [key])
        return
    total.append(novo_indice)
    return
