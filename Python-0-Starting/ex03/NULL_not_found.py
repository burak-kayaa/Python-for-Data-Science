# def NULL_not_found(object: any) -> int:
#     typ = type(object)
#     name = typ.__name__
#     title = name.title()
#     # print(f"{object} : {title}")
#     print(f"{object} : {object.__class__}")


def NULL_not_found(object: any) -> int:
    typ = type(object)
    name = typ.__name__
    # print(f"name: {name}")
    if (name == "NoneType" and object == None):
        title = "Nothing:"
    elif (name == "float" and object != object):
        title = "Cheese:"
    elif (name == "int" and object == 0):
        title = "Zero:" 
    elif (name == "str" and object == ""):
        title = "Empty:"
    elif (name == "bool" and object == False):
        title = "Fake:"
    else:
        print("Type not Found")
        return 1
    print(f"{title} {object} {object.__class__}")
    return 0
