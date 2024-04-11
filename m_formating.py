def removeSpacesAndCapitalize(origin:str, ifCapitalize:bool = True):
    origin = origin.strip()

    if ifCapitalize:
        origin = origin.capitalize()

    return origin