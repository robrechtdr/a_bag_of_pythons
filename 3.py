def to_dict_zip(l1, l2):
    """
    A known problem with docstring tests is that for unordered objects like 
    dicts test fail if the order of items returned happens to be different 
    than in the doctest and thus will seemingly randomly fail unless checked
    against an ordered output.
    See: http://www.ianbicking.org/blog/2012/10/why-doctestjs-is-better-than-pythons-doctest.html
    #>>> to_dict_zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4])
    #{'a': 1, 'c': 3, 'b': 2, 'd': 4}

    #>>> to_dict_zip(['a', 'b', 'c', 'd'], [1, 2, 3])
    #{'a': 1, 'c': 3, 'b': 2}

    #>>> to_dict_zip(['a', 'b', 'c'], [1, 2, 3, 4])
    #{'a': 1, 'c': 3, 'b': 2}


    Bonus points if you can explain how you'd deal with lists of different lengths:

    See above examples; key-value pair aren't added in the resulting dictionary if 
    either the prospecting key or value is missing.
    """
    return dict(zip(l1, l2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
