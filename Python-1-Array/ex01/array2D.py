def check_lists(lists: list) -> int:
    """
    Check if all inner lists in a 2D list have the same length.

    Parameters
    ----------
    lists : list
        A 2D list to check.

    Returns
    -------
    int
        1 if the inner lists have different lengths or the input is None,
        0 if all inner lists have the same length.
    """
    if lists is None:
        return 1
    for elem in lists:
        if elem is None:
            return 1
    for elem in lists:
        if not isinstance(elem, list):
            return 1
    first_len = len(lists[0])
    for elem in lists:
        if len(elem) != first_len:
            return 1
    return 0


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list between start and end indices,
    ensuring all inner lists have the same length.

    Parameters
    ----------
    family : list
        A 2D list where each inner list should have the same length.
    start : int
        The starting index for slicing (inclusive).
    end : int
        The ending index for slicing (exclusive).

    Returns
    -------
    list
        The sliced 2D list, or None if the inner lists have different lengths.
    """
    if check_lists(family):
        return None
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    x = slice(start, end)
    sliced_list = family[x]
    print(f"My new shape is : ({len(sliced_list)}, {len(sliced_list[0])})")
    return sliced_list
