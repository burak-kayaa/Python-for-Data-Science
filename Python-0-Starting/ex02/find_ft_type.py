def all_thing_is_obj(object: any) -> int:
    minishell = {
        "List": "list",
        "Tuple": "tuple",
        "Dict": "dict",
        "Set": "set",
        "Str": "str",
    }
    typ = type(object)
    name = typ.__name__
    name = name[0].upper() + name[1:]
    # name = typeps.get(typ.__name__, None)
    if minishell.get(name) is None:
        print("Type not found")
    elif name == "Str":
        print(f"{object} is in the kitchen : {object.__class__}")   
    else:
        print(f"{name} : {object.__class__}")
    return 42
