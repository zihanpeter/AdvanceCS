def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxCnt = 0
    res = ''
    for key, value in aDict.items():
        if len(value) > maxCnt:
            maxCnt = len(value)
            res = key
    return res

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}


animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

biggest(animals)





