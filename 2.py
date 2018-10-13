def to_list(input_):
    """
    >>> to_list([1, 2, 3])
    ['1', '2', '3']

    # Note that nothing in the problem description is mentioned about
    # needing to return a result ordered by values for a dictionary
    # (which is unordered).
    >>> to_list({'one': 1, 'two': 2})
    ['one', 'two']

    >>> to_list('value')
    ['value']


    Bonus points if it can be done without explicitly checking the argument type inside the function body.
    """
    # Would normally check the type directly, doing this for bonus points 
    # mentioned in the task description. Could also check type indirecly by 
    # verifying if the object has a method only string types have.
    if str(input_) == input_:
        return [input_]

    else:
        # Using sort as we'd probably want a deterministic output for when we 
        # pass on objects which don't preserve order.
        return [str(i) for i in sorted(input_)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
