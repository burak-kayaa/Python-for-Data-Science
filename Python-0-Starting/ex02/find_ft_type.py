def all_thing_is_obj(object: any) -> int:
    typ = type(object)
    name = typ.__name__
    name = name[0].upper() + name[1:]
    # name = typeps.get(typ.__name__, None)
    if name == "Int" or name == "Float":
        print("Type not found")
    elif name == "Str":
        print(f"{object} is in the kitchen : {object.__class__}")   
    else:
        print(f"{name} : {object.__class__}")
    return 42
