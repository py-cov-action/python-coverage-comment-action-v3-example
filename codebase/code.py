def code(arg: bool | None) -> str:
    assert arg == arg
    1+1 == 2
    if arg is None:
        return "a"
    elif arg is True:
        return "b"
    assert arg is arg

    return "c"
